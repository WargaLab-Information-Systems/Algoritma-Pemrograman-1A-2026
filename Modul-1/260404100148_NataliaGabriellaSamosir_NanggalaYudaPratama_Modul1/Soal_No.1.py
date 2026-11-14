
# Program Menghitung Total Pembayaran

# Deklarasi variabel
banyakBuku = 0
banyakPulpen = 0
banyakFD = 0
subTotal = 0
diskon = 0
hargaSetelahDiskon = 0
pajak = 0
totalBayar = 0
banyakUang = 200000
kembalian = 0

# Input jumlah barang
print("=== PROGRAM KASIR ===")
banyakBuku = int(input("Masukkan banyak buku: "))
banyakPulpen = int(input("Masukkan banyak pulpen: "))
banyakFD = int(input("Masukkan banyak FD: "))

# Menghitung harga setiap barang
hargaBuku = banyakBuku * 25000
hargaPulpen = banyakPulpen * 8000
hargaFD = banyakFD * 75000

# Menghitung subtotal
subTotal = hargaBuku + hargaPulpen + hargaFD

# Menghitung diskon 10%
diskon = subTotal * 10 / 100

# Menghitung harga setelah diskon
hargaSetelahDiskon = subTotal - diskon

# Menghitung pajak 11%
pajak = hargaSetelahDiskon * 11 / 100

# Menghitung total pembayaran
totalBayar = hargaSetelahDiskon + pajak

# Menghitung uang kembalian
kembalian = banyakUang - totalBayar

# Menampilkan hasil
print("\n=== STRUK PEMBAYARAN ===")
print("Harga Buku          : Rp", hargaBuku)
print("Harga Pulpen        : Rp", hargaPulpen)
print("Harga FD            : Rp", hargaFD)
print("Subtotal            : Rp", subTotal)
print("Diskon 10%          : Rp", diskon)
print("Harga Setelah Diskon: Rp", hargaSetelahDiskon)
print("Pajak 11%           : Rp", pajak)
print("Total Bayar         : Rp", totalBayar)
print("Uang Dibayarkan     : Rp", banyakUang)
print("Kembalian           : Rp", kembalian)
