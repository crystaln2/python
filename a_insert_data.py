import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "toko_buah"
)
nama = input("Masukan nama buah: ")
asal = input("Masukan asal buah (Lokal atau Impor): ")
stok = input("Masukan stok buah: ")
harga_satuan = input("Masukan harga buah satuan: ")
val = (nama, asal, stok, harga_satuan)
cursor = db.cursor()
sql = "INSERT INTO stok_buah (nama, asal, stok, harga_satuan) VALUES (%s, %s, %s, %s)"
cursor.execute(sql, val)
db.commit()
print("{} data berhasil disimpan".format(cursor.rowcount))