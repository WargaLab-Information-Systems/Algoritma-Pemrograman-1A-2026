# Program Diskon Supermarket "Koperasi Ndeso"

total = int(input("Masukkan total harga barang : Rp"))
print("Total belanja awal: Rp", total)

# Mengecek diskon
if total % 100000 == 0:
    bayar = 0 # Diskon 100%
elif total % 50000 == 0:
    bayar = total * 50  // 100 # Diskon 50%
elif total % 10000 == 0:
    bayar = total * 80 // 100 #Diskon 20%
elif total >= 200000:
    bayar = total * 90 // 100 #Diskon 10%
else: 
    bayar = total
print ("Total harga akhir: Rp", bayar)

# Ternary operator
poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin:", poin)