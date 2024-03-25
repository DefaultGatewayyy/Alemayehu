import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="78466487Ms",
    database="Medarbejder"
)

cursorObject = mydb.cursor()
cursorObject.execute("CREATE TABLE Rapport (Id INT PRIMARY KEY AUTO_INCREMENT, Fornavn VARCHAR(255), Efternavn VARCHAR(255), Adresse VARCHAR(255), ByNavn VARCHAR(255), Postnummer INT, Email VARCHAR(255), Telefonnummer INT, Alder INT, Uddannelse VARCHAR(255), Kørekort VARCHAR(255), CPR_Nummer VARCHAR(255))")

