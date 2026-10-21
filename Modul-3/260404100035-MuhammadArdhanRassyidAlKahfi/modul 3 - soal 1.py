
jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    try:
        input_jarak = input("Masukkan jarak penumpang (km), 0 untuk selesai: ")

        # Mengecek input kosong
        if input_jarak.strip() == "":
            print("Input tidak boleh kosong. Silakan masukkan jarak dalam angka.")
            continue

        jarak = int(input_jarak)

        # Mengecek angka negatif
        if jarak < 0:
            print("Jarak tidak boleh negatif, masukkan ulang!")
            continue

        # Mengakhiri input jika jarak 0
        if jarak == 0:
            break

    except ValueError:
        print("Tolong masukkan angka, bukan teks atau kalimat.")
        continue

    # Menghitung tarif
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah_penumpang += 1

    # Diskon setiap penumpang ke-5
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5

    total_pendapatan += tarif
    total_jarak += jarak

    # Menentukan jarak terjauh
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

# Menghitung rata-rata jarak
if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
else:
    rata_rata = 0

# Menampilkan hasil
print("Jumlah penumpang:", jumlah_penumpang)
print("Total pendapatan: Rp", total_pendapatan)
print("Jarak terjauh:", jarak_terjauh, "km")
print("Rata-rata jarak:", rata_rata, "km")