import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "78466487Ms")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Medarbejder")