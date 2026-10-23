jumlah = 0
total = 0
total_jarak = 0
terjauh = 0

while True:
    jarak = int(input("Masukkan jarak (km), 0 untuk selesai: "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    jumlah = jumlah + 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlah % 5 == 0:
        tarif = tarif / 2
        print("Diskon 50%!")

    print("Tarif: Rp", tarif)

    total = total + tarif
    total_jarak = total_jarak + jarak
    if jarak > terjauh:
        terjauh = jarak

print("\n--- Rekap ---")
print("Jumlah penumpang:", jumlah)
print("Total pendapatan: Rp", total)

if jumlah > 0:
    print("Jarak terjauh:", terjauh, "km")
    print("Rata-rata jarak:", total_jarak / jumlah, "km")