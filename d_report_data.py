import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "toko_buah"
)

cursor = db.cursor()
impor = "SELECT SUM(stok) FROM stok_buah WHERE asal = 'Impor'"
lokal = "SELECT SUM(stok) FROM stok_buah WHERE asal = 'Lokal'"
minimal = "SELECT MIN(stok) FROM stok_buah"
cursor.execute(impor)
result_impor = cursor.fetchone()
cursor.execute(lokal)
result_lokal = cursor.fetchone()
cursor.execute(minimal)
result_minimal = cursor.fetchone()
print("Total stok impor: " + str(result_impor))
print("Total stok lokal: " + str(result_lokal))
print("Stok paling sedikit: " + str(result_minimal))