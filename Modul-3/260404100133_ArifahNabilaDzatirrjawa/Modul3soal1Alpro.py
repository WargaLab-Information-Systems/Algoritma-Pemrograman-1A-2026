jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = int(input("Masukkan jarak yang ditempuh (km), ketik '0' untuk selesai: "))
    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak yang Diinput Tidak Valid!")
        continue

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah_penumpang = jumlah_penumpang + 1

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Diskon 50% Diberikan!")

    print("Tarif: Rp", tarif)

    total_pendapatan = total_pendapatan + tarif
    total_jarak = total_jarak + jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("Jumlah Penumpang:", jumlah_penumpang)
print("Total Pendapatan: Rp", total_pendapatan)
print("Jarak Terjauh yang Ditempuh (km):", jarak_terjauh)

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Rata-Rata Jarak yang Ditempuh (km):", rata_rata)
else:
    print("Rata-Rata Jarak yang Ditempuh: 0 km")
