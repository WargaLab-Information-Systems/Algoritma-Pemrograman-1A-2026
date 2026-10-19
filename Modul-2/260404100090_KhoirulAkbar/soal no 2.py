total = int(input("Masukkan total belanja: Rp "))

# Menentukan diskon
if total % 100000 == 0: #modulus 100 rb di gunakan untuk mencari kelipatan 100 rb 
    bayar = 0
elif total % 50000 == 0:
    bayar = total - (total * 50 // 100)
elif total % 10000 == 0:
    bayar = total - (total * 20 // 100)
elif total >= 200000:
    bayar = total - (total * 10 // 100)
else:
    bayar = total

# Status poin menggunakan ternary operator
if bayar > 0 :
    poin = "Poin Bertambah"
else :
    poin = "Tidak Ada Poin"

# Menampilkan hasil
print("Total belanja awal : Rp", total)
print("Total yang dibayar : Rp", bayar)
print("Status poin        :", poin)