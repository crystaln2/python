import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "toko_buah"
)

cursor = db.cursor()
id = input("Pilih id buah: ")
stok = input("Stok buah baru: ")


sql = "UPDATE stok_buah SET stok=%s WHERE id=%s"
val = (stok, id)
cursor.execute(sql, val)
db.commit()
print("{} data berhasil diubah".format(cursor.rowcount))