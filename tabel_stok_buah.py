import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "toko_buah"
)

cursor = db.cursor()
sql = """CREATE TABLE stok_buah (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255), asal Varchar(255), stok INT, harga_satuan INT
)
"""
cursor.execute(sql)

print("Tabel stok_buah berhasil dibuat!")