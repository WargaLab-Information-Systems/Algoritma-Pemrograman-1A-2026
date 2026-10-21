# input total belanja awal sebelum diskon
totalBelanja =int(input("masukkan total belanja siti (Rp): "))

# harga akhir total bayar setelah pengecekan diskon
if totalBelanja % 100000 == 0:
    print("maka siti tidak perlu membayar/gratis")
    totalBayar = 0
elif totalBelanja % 50000 == 0:
    print("maka siti mendapatkan diskon 50% ")
    totalBayar = totalBelanja * 0.5
elif totalBelanja % 10000 == 0:
    print("maka siti mendapatkan diskon 20% ")
    totalBayar = totalBelanja * 0.8
elif totalBelanja >= 200000:
    print("maka siti mendapatkan diskon 10% ")
    totalBayar = totalBelanja * 0.9 
else:
    print("maka siti membayar dengan harga normal ")
    totalBayar = totalBelanja

print("total harga akhir: Rp", int(totalBayar))

# operator tenary
status ="poin bertambah" if totalBayar > 0 else "tidak ada poin"
print("status totalBayar siti adalah:", status )