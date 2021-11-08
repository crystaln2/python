import mysql.connector #melakukan koneksi ke MySQL
import os #keluar dari aplikasi
import matplotlib.pyplot as plt #untuk membuat grafik
import pandas as pd #untuk mengekspor data 

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_buah",
  use_pure=True #melambangkan implementasi Python
)


def insert_data(db):
  nama = input("Masukan nama buah: ")
  asal = input("Masukan asal buah (Lokal atau Impor): ")
  stok = input("Masukan stok buah: ")
  harga_satuan = input("Masukan harga buah satuan: ")
  val = (nama, asal, stok, harga_satuan)
  
  #menghapus data akan melanjutkan nilai auto increment tanpa memperdulikan ada angka yang terlewati akibat penghapusan data
  #oleh karena itu auto increment direset agar tetap menghitung mulai dari 1
  #reset dapat dilakukan dengan menggunakan "ALTER TABLE table_name AUTO_INCREMENT = 1"
  cursor = db.cursor()
  reset_1 = "ALTER TABLE stok_buah AUTO_INCREMENT = 1" 
  cursor.execute(reset_1)
  db.commit()

  cursor = db.cursor()
  sql = "INSERT INTO stok_buah (nama, asal, stok, harga_satuan) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()

  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM stok_buah"
  cursor.execute(sql)
  
  results = cursor.fetchall() #fetchall akan menampilan semua data pada tabel, untuk menampilkan 1 data digunakan fetchone

  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db) #data ditampilkan terlebih dahulu agar pengguna aplikasi dapat memilih data mana yang akan diganti
  id = input("Pilih id buah: ")
  stok = input("Stok buah baru: ") 

  sql = "UPDATE stok_buah SET stok=%s WHERE id=%s" #stok buah yang baru akan ter-update sesuai id yan dipilih oleh pengguna
  val = (stok, id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))



def chart_data(db):
  #chart 1 : hubungan antara buah dengan stok buah
  fig = plt.figure() #chart akan muncul dalam bentuk gambar
  fig.suptitle("Buah vs Stok buah") #judul chart
  ax = fig.add_axes([0,0,1,1])
  Buah = ['Apel', 'Pisang', 'Jeruk', 'Pir', 'Rambutan', 'Anggur', 'Lemon', 'Sawo', 'Salak', 'Jambu']
  Stok = [20, 30, 40, 25, 30, 10, 12, 15, 25, 20]
  ax.bar(Buah, Stok) #bentuk chat yang diinginkan, 'bar' dapat diganti menjadi 'pie' atau 'plot' jika menginginkan bentuk chart berupa pie atau plot
  plt.show()
  
  #chart 2 : hubungan antara buah dengan harga satuannya
  fig = plt.figure()
  fig.suptitle("Buah vs Harga satuan")
  ax = fig.add_axes([0,0,1,1])
  Buah = ['Apel', 'Pisang', 'Jeruk', 'Pir', 'Rambutan', 'Anggur', 'Lemon', 'Sawo', 'Salak', 'Jambu']
  Harga_satuan = [32000, 15000, 25000, 21000, 12000, 40000, 35000, 15000, 12000, 10000]
  ax.bar(Buah, Harga_satuan)
  plt.show()

  #setelah dieksekusi, akan ditampilkan 2 buah chart berupa gambar


def export_data (db):
  try:
      query = "SELECT * FROM stok_buah"
      result_dataFrame = pd.read_sql(query,db)
      result_dataFrame.to_csv('Tabel Stok Buah.csv') #ganti nama file setiap melakukan export data, jika nama sama, mungkin proses akan gagal
    
  except Exception as e:
      print(str(e))

def report_data(db):
  cursor = db.cursor()
  impor = "SELECT SUM(stok) FROM stok_buah WHERE asal = 'Impor'"
  lokal = "SELECT SUM(stok) FROM stok_buah WHERE asal = 'Lokal'"
  minimal = "SELECT MIN(stok) FROM stok_buah"

  cursor.execute(impor)
  result_impor = cursor.fetchone() #total stok impor

  cursor.execute(lokal)
  result_lokal = cursor.fetchone() #total stok lokal

  cursor.execute(minimal)
  result_minimal = cursor.fetchone() #nilai minimal (stok)

  print("Total stok impor: " + str(result_impor))
  print("Total stok lokal: " + str(result_lokal))
  print("Stok paling sedikit: " + str(result_minimal))


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("a. Insert Data")
  print("b. Tampilkan Data")
  print("c. Update Data")
  print("d. Laporan Data")
  print("e. Grafik Data")
  print("f. Export data ke .CSV format")
  print("g. Keluar")
  print("------------------")
  menu = input("Pilih menu (a-g): ")

  #clear screen
  os.system("clear")
  
  #pengguna meng-input menu yang dipilih (dari a sampai g)
  if menu == "a":  
    insert_data(db)
  elif menu == "b":
    show_data(db)
  elif menu == "c":
    update_data(db)
  elif menu == "d":
    report_data(db)
  elif menu == "e":
    chart_data(db)
  elif menu == "f":
    export_data(db)
  elif menu == "g":
    exit()
  else: #pengguna meng-input selain a-g, sehingga else dijalankan karena bernilai false
    print("Menu salah!")


if __name__ == "__main__":
  while(True): #loop agar code pada def dapar dijalankan (jika bernilai true)
    show_menu(db)