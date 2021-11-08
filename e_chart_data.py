import matplotlib.pyplot as plt
fig = plt.figure()
fig.suptitle("Buah vs Stok buah")
ax = fig.add_axes([0,0,1,1])
Buah = ['Apel', 'Pisang', 'Jeruk', 'Pir', 'Rambutan', 'Anggur', 'Lemon', 'Sawo', 'Salak', 'Jambu']
Stok = [20, 30, 40, 25, 30, 10, 12, 15, 25, 20]
ax.bar(Buah, Stok)
plt.show()

fig = plt.figure()
fig.suptitle("Buah vs Harga satuan")
ax = fig.add_axes([0,0,1,1])
Buah = ['Apel', 'Pisang', 'Jeruk', 'Pir', 'Rambutan', 'Anggur', 'Lemon', 'Sawo', 'Salak', 'Jambu']
Harga_satuan = [32000, 15000, 25000, 21000, 12000, 40000, 35000, 15000, 12000, 10000]
ax.bar(Buah, Harga_satuan)
plt.show()