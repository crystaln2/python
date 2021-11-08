import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "toko_buah"
)

cursor = db.cursor()
reset_1 = "ALTER TABLE stok_buah AUTO_INCREMENT = 1"
cursor.execute(reset_1)

db.commit()

print("Auto increment dimulai kembali menjadi 1")