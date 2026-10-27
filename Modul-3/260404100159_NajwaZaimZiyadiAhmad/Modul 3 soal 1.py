
print("=== PROGRAM TARIF PENUMPANG BUS ===")

jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = float(input("Masukkan jarak tempuh (km), 0 untuk selesai: "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid! Silakan masukkan ulang.")
        continue

    jumlah_penumpang += 1
    total_jarak += jarak

    # Menghitung tarif berdasarkan jarak
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    # Diskon 50% setiap penumpang ke-5
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Selamat! Mendapat diskon 50%.")

    total_pendapatan += tarif

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print(f"Tarif penumpang: Rp{tarif:,.0f}")

print("\n=== HASIL AKHIR ===")
print("Jumlah penumpang:", jumlah_penumpang)
print(f"Total pendapatan: Rp{total_pendapatan:,.0f}")

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Jarak terjauh:", jarak_terjauh, "km")
    print(f"Rata-rata jarak: {rata_rata:.2f} km")
else:
    print("Belum ada penumpang yang dihitung.")




