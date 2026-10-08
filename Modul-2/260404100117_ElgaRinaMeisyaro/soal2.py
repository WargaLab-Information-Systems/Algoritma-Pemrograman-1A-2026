# Program Diskon Supermarket "Koperasi Ndeso"

# Input jumlah jenis barang
# jumlah_barang = int(input("Masukkan jumlah jenis barang :"))
print("Jumlah Barang Yang Bu Siti Beli Sebanyak 3 Barang")
total_belanja = 0 

# Menghitung total belanja 
harga1 = int(input("Masukkan harga barang 1: Rp"))
harga2 = int(input("Masukkan harga barang 2: Rp"))
harga3 = int(input("Masukkan harga barang 3: Rp"))

#Menghitung total belanja 
total = harga1 + harga2 + harga3
print("Total belanja awal: Rp", total)

# Mengecek diskon
if total % 100000 == 0:
    bayar = total * 90 // 100 # Diskon 10%
elif total % 50000 == 0:
    bayar = total * 95  // 100 # Diskon 5%
elif total >= 200000:
    bayar = total * 90 // 100 
else: 
    bayar = total
print ("Total harga akhir: Rp", bayar)

# Ternary operator
poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin:", poin)