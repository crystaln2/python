import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = ""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_buah")

print ("Database toko_buah berhasil dibuat!")