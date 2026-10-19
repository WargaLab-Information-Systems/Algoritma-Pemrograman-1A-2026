# Variabel untuk menyimpan data
jumlah = 0       # jumlah penumpang
total = 0        # total pendapatan
total_jarak = 0  # untuk menghitung rata-rata
terjauh = 0      # jarak terjauh

while True:
    jarak = int(input("Masukkan jarak (km), 0 untuk selesai: "))

    # Berhenti jika 0
    if jarak == 0:
        break

    # Jarak negatif tidak valid, ulangi
    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    # Penumpang valid, tambah hitungan
    jumlah = jumlah + 1

    # Hitung tarif sesuai jarak
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    # Diskon 50% untuk penumpang ke-5, 10, 15, dst
    if jumlah % 5 == 0:
        tarif = tarif / 2
        print("Diskon 50%!")

    print("Tarif: Rp", tarif)

    # Perbarui data
    total = total + tarif
    total_jarak = total_jarak + jarak
    if jarak > terjauh:
        terjauh = jarak

# Tampilkan hasil akhir
print("\n--- Rekap ---")
print("Jumlah penumpang:", jumlah)
print("Total pendapatan: Rp", total)

if jumlah > 0:
    print("Jarak terjauh:", terjauh, "km")
    print("Rata-rata jarak:", total_jarak / jumlah, "km")