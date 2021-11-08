import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "toko_buah"
)
cursor = db.cursor()
sql = "INSERT INTO stok_buah (nama, asal, stok, harga_satuan) VALUES (%s, %s, %s, %s)"
values = [
  ("Apel", "Impor", 20, 32000),
  ("Pisang", "Lokal", 30, 15000),
  ("Jeruk", "Lokal", 40, 25000),
  ("Pir", "Impor", 25, 21000),
  ("Rambutan", "Lokal", 30, 12000),
  ("Anggur", "Impor", 10, 40000),
  ("Lemon", "Impor", 12, 35000),
  ("Sawo", "Lokal", 15, 15000),
  ("Salak", "Lokal", 25, 12000),
  ("Jambu", "Lokal", 20, 10000)
  
]

for val in values:
  cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))