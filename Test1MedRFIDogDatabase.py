#DENNE KODE SIMULERE DET AT BRUGE ET RFID TAG KODE DEN MED DATA FRA EN DATA BASE OG LÆSE DET IND I EN ANDEN


import mysql.connector

def opret_forbindelse_til_database(database_navn):
    try:
        forbindelse = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78466487Ms",
            database="Brandmand"
        )
        print(f"Forbindelse til {database_navn}-databasen oprettet!")
        return forbindelse
    except mysql.connector.Error as fejl:
        print(f"Fejl ved oprettelse af forbindelse til {database_navn}-databasen:", fejl)
        return None

def hent_data_til_rfid(forbindelse_kilde):
    if forbindelse_kilde is None:
        return None

    try:
        cursor = forbindelse_kilde.cursor()

        # Hent data fra kilde-databasen (f.eks. Brandmand-databasen)
        cursor.execute("SELECT * FROM Ansatte_Deltid_Brandmænd")
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as fejl:
        print("Fejl ved hentning af data fra kilde-databasen:", fejl)
        return None

def skriv_data_til_rfid(rfid_data):
    # Simulér processen med at skrive data til en RFID-tag
    print(f"Data skrevet til RFID-tag: {rfid_data}")

def læs_rfid_data():
    # Simulér læsning af data fra en RFID-tag
    rfid_data = input("Indtast RFID-data læst fra RFID-læseren: ")
    return rfid_data

def indsæt_data_i_database(forbindelse_mål, data):
    if forbindelse_mål is None or data is None:
        return

    try:
        cursor = forbindelse_mål.cursor()

        # Indsæt data i destinations-databasen (f.eks. DestinationsDatabase)
        sql_insert = "INSERT INTO Rapport (Fornavn, Efternavn, Adresse, ByNavn, Postnummer, Email, Telefonnummer, Alder, Uddannelse, Kørekort, CPR_Nummer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql_insert, data)
        forbindelse_mål.commit()
        print("Data er blevet indsat i destinations-databasen!")
    except mysql.connector.Error as fejl:
        print("Fejl ved indsættelse af data i destinations-databasen:", fejl)

def hovedprogram():
    # Opret forbindelse til kilde-databasen (f.eks. Brandmand-databasen)
    kilde_database = opret_forbindelse_til_database("Brandmænd")

    # Opret forbindelse til destinations-databasen (f.eks. UdrykningsRapport)
    destinations_database = opret_forbindelse_til_database("UdrykningsRapport")

    if kilde_database and destinations_database:
        # Hent data fra kilde-databasen (f.eks. Brandmand-databasen)
        data = hent_data_til_rfid(kilde_database)

        if data:
            # Skriv data til RFID-tag (simuleret)
            skriv_data_til_rfid(data)

            # Læs data fra RFID-tag med en RFID-læser (simuleret)
            rfid_data = læs_rfid_data()

            # Indsæt data i destinations-databasen (f.eks. UdrykningsRapport)
            indsæt_data_i_database(destinations_database, data)

        kilde_database.close()
        destinations_database.close()
        print("Forbindelserne til databaserne er blevet lukket.")

if __name__ == "__main__":
    hovedprogram()

#For at kopiere data fra den ene database til en RFID-tag og derefter læse den RFID-tag med en læser og indsætte dataene i den anden database, kan du bruge følgende tilgang:


#Denne kode simulerer processen med at hente data fra en kilde-database, skrive det til en RFID-tag, læse dataene fra RFID-taggen med en læser og indsætte dataene i destinations-databasen. Husk at erstatte "Brandmand" med navnet på din kilde-database og "DestinationsDatabase" med navnet på din destinations-database.