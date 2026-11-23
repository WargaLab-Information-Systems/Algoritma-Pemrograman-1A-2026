reguler = 40000
VIP = 75000
VIIP 100000
totalTiket = reguler + VIP + VIIP

jenisTiket = 0
jenisTiket = jenisTiket + 1

reguler = input("tambahan minuman seharga 10000/tiket (y/n): ")
VIP = "mendapatkan minuman gratis"
VIIP = "mendapatkan minuman gratis"
print(VIP)
print(VIIP)

if totalTiket >= 3:
    if membercard:
        diskon = 15/100
    else:
        diskon = 10/100

uang = int(input("masukkan nominal uang: "))
if uang <= totalTiket:
   kembalian = uang - totalTiket

print("kembaliannya yaitu", kembalian)

"""
bioskop menyediakan 3 tiket yaitu regular, VIP, VIIP. Pelanggan bisa membeli lebih dari satu tiket, tiket regular menawarkan jika ada tambahan minuman seharga 10000, sedangkan Vip dan viip gratis

"""
