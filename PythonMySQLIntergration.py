import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78466487Ms",
            database="Brandmand"
        )
        print("Forbindelse til MySQL-databasen oprettet!")
        return connection
    except mysql.connector.Error as error:
        print("Fejl ved oprettelse af forbindelse til MySQL:", error)
        return None

def fetch_brandmænd(connection):
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Ansatte_Deltid_Brandmænd")
        brandmænd = cursor.fetchall()
        print("Liste over Deltid's Ansætte Brandmænd:")
        for brandmand in brandmænd:
            print(brandmand)
    except mysql.connector.Error as error:
        print("Fejl ved hentning af data fra MySQL-tabellen:", error)

def insert_brandmænd(connection, firstname, lastname, address, city, postalcode, email, phonenumber, age, education, drivinglicense, cprnumber):
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Ansatte_Deltid_Brandmænd (Fornavn, Efternavn, Adresse, ByNavn, Postnummer, Email, Telefonnummer, Alder, Uddannelse, Kørekort, CPR_Nummer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (firstname, lastname, address, city, postalcode, email, phonenumber, age, education, drivinglicense, cprnumber)
        cursor.execute(sql, val)
        connection.commit()
        print("Ny Brandmand er blevet indsat i databasen!")
    except mysql.connector.Error as error:
        print("Fejl ved indsættelse af data i MySQL-tabellen:", error)

def main():
    connection = connect_to_database()
    if connection:
        fetch_brandmænd(connection)
        choice = input("Vil du indsætte en ny brandmand? (ja/nej): ")
        if choice.lower() == "ja":
            firstname = input("Indtast Fornavn: ")
            lastname = input("Indtast Efternavn: ")
            age = int(input("Indtast Alder: "))
            cprnumber = int(input("Indtast CPR Nummer: "))
            address = input("Indtast Adresse: ")
            city = input("Indtast ByNavn: ")
            postalcode = int(input("Indtast Postnummer: "))
            email = input("Indtast Email: ")
            phonenumber = int(input("Indtast Telefonnummer: "))
            education = input("Indtast Uddannelse: ")
            drivinglicense = input("Indtast Kørekort: ")
            insert_brandmænd(connection, firstname, lastname, address, city, postalcode, email, phonenumber, age, education, drivinglicense, cprnumber)
        connection.close()
        print("Forbindelsen til MySQL-databasen er lukket.")

if __name__ == "__main__":
    main()
