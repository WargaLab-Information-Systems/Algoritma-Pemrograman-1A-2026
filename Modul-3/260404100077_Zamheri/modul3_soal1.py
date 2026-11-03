
jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = float(input("Masukkan jarak tempuh (km) :"))

    if jarak == 0:
        break


    if jarak < 0:
        print("Jarak tidak valid! Silakan masukkan ulang.")
        continue

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah_penumpang += 1

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Selamat! Penumpang mendapat diskon 50%.")

    total_pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print(f"Tarif yang harus dibayar: Rp{tarif}")


print(f"Jumlah penumpang   : {jumlah_penumpang}")
print(f"Total pendapatan   : Rp{total_pendapatan}")
print(f"Jarak terjauh      : {jarak_terjauh} km")

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print(f"Rata-rata jarak    : {rata_rata} km")
else:
    print("Rata-rata jarak    : 0 km")
