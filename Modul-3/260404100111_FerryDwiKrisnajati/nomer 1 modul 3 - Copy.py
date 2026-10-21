jumlah = 0
total = 0
total_jarak = 0
terjauh = 0
nomor = 0

while True:
    jarak = float(input("Masukkan jarak: "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    nomor = nomor + 1
    jumlah = jumlah + 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if nomor % 5 == 0:
        tarif = tarif * 0.5

    total = total + tarif
    total_jarak = total_jarak + jarak

    if jarak > terjauh:
        terjauh = jarak

if jumlah > 0:
    rata = total_jarak / jumlah
else:
    rata = 0

print("Jumlah penumpang :", jumlah, "orang")
print("Total pendapatan : Rp", total)
print("Jarak terjauh    :", terjauh, "Km")
print("Rata-rata jarak  :", rata, "Km")
print("penumpang ke-", nomor, "mendapat diskon 50%")