import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "toko_buah"
)

cursor = db.cursor()
sql = "SELECT * FROM stok_buah"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)