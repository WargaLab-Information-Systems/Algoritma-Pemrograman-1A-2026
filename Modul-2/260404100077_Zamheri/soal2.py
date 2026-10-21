total = int(input("Masukkan total belanja : Rp"))

if total % 100000 == 0:
    diskon = 100
elif total % 50000 == 0:
    diskon = 50
elif total % 10000 == 0:
    diskon = 20
elif total >= 200000:
    diskon = 10
else:
    diskon = 0

potongan = total * diskon / 100
bayar = total - potongan

print("Total belanja awal : Rp", total)
print("Diskon :", diskon, "%")
print("Potongan harga : Rp", int(potongan))
print("Total harga akhir : Rp", int(bayar))
poin = "poin bertambah" if bayar > 0 else "tidak ada point"

print ("Status poin :",poin)