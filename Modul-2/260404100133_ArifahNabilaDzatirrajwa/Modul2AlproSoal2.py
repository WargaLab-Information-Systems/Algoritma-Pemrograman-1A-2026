total_belanja = int(input("Masukkan total belanja: "))

print("Total belanja awal : Rp", total_belanja)

if total_belanja % 100000 == 0:
    print("SITI mendapatkan diskon 100% (Gratis)")
    total_bayar = 0
elif total_belanja % 50000 == 0:
    print("SITI mendapatkan diskon 50%")
    total_bayar = total_belanja * (50 // 100)
elif total_belanja % 10000 == 0:
    print("SITI mendapatkan diskon 20%")
    total_bayar = total_belanja * (80 // 100)
elif total_belanja >= 200000:
    print("SITI mendapatkan diskon 10%")
    total_bayar = total_belanja * (90 // 100)
else:
    print("SITI tidak mendapatkan diskon")
    total_bayar = total_belanja

print("Total harga akhir  : Rp", total_bayar)

poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("Status poin: ", poin)