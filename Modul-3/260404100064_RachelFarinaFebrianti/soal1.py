jumlah = 0
total = 0
total_jarak = 0
terjauh = 0

while True:
    jarak = int(input("Masukkan jarak tempuh (km, 0 untuk selesai): "))
    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, ulangi input!")
        continue
    jumlah = jumlah + 1
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
    if jumlah % 5 == 0:
        tarif = tarif * 50 / 100
        print("Penumpang ke-", jumlah, "mendapat diskon 50%")
    total = total + tarif
    total_jarak = total_jarak + jarak
    if jarak > terjauh:
        terjauh = jarak
    print("Tarif penumpang ke-", jumlah, ": Rp", tarif)

print("Jumlah penumpang :", jumlah)
print("Total pendapatan : Rp", total)
print("Jarak terjauh :", terjauh, "km")
rata = total_jarak / jumlah if jumlah > 0 else 0
print("Rata-rata jarak :", rata, "km")
