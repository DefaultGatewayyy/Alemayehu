#!/usr/bin/env python

import time
import smbus2
import sqlite3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

from RPLCD.i2c import CharLCD
# Definer LCD'et
lcd = CharLCD(i2c_expander='PCF8574', address=0x23, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

# Opret forbindelse til databasen
conn = sqlite3.connect('rfid_data.db')
cursor = conn.cursor()
# Opret en tabel til at gemme RFID-data, hvis den ikke allerede findes
cursor.execute('''CREATE TABLE IF NOT EXISTS rfid_tags (
                id INTEGER PRIMARY KEY,
                tag_id TEXT,
                tag_data TEXT
                )''')
# Gem ændringerne og luk forbindelsen til databasen
conn.commit()

def WRITE():
    try:
        medarbejdernummer = input('Indtast medarbejdernummer: ')
        navn = input('Indtast navn: ')
        alder = input('Indtast alder: ')
        kompetence_niveau = input('Indtast kompetenceniveau: ')
        kørerkort_niveau = input('Indtast kørekortniveau: ')
        
        # Saml alle data i en streng
        text = "Medarbejdernummer: {}, Navn: {}, Alder: {}, Kompetenceniveau: {}, Kørerkortniveau: {}".format(medarbejdernummer, navn, alder, kompetence_niveau, kørerkort_niveau)

        # Juster længden af tekststrengen, så den passer til blokkene på RFID-tags
        text = text.ljust(len(reader.BLOCK_ADDRS) * 16)[:len(reader.BLOCK_ADDRS) * 16]

        # Hvis text er en bytes-objekt, konverter den til en streng
        if isinstance(text, bytes):
            text = text.decode('utf-8')

        # Skriv dataen til RFID-taggen
        reader.write(text)

        print("Dataen er blevet skrevet")
    finally:
        GPIO.cleanup()

def READ():
    try:
        while True:
            id, text = reader.read()

            # Udskriv data til konsollen
            print("RFID Tag ID:", id)
            print("Data:", text)

            # Ryd LCD-displayet
            lcd.clear()

            # Skriv RFID-tagens ID på første linje
            lcd.write_string("ID: {}".format(id))

            # Skriv teksten fra RFID-taggen på anden linje
            lcd.cursor_pos = (1, 0)
            lcd.write_string("Text: {}".format(text))

            # Gem dataene i databasen
            cursor.execute("INSERT INTO rfid_tags (tag_id, tag_data) VALUES (?, ?)", (id, text))
            conn.commit()

            time.sleep(2)  # Vent 2 sekunder før næste læsning

    finally:
        # Luk forbindelsen til databasen
        conn.close()
        lcd.close()