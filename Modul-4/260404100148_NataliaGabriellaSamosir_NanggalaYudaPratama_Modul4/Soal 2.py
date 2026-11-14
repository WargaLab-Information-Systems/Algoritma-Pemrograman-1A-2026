
print("=== PROGRAM GAJI MINGGUAN KARYAWAN ===")

gaji_pokok = 100000
bonus_malam = 50000
total_gaji = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    # Input jam lembur dengan validasi
    while True:
        lembur = int(input("Masukkan jam lembur: "))

        if lembur < 0 or lembur > 8:
            print("Jumlah lembur melebihi batas atau tidak valid!")
            print("Silakan masukkan ulang.")

        elif lembur not in [0, 1, 2, 3, 4, 6, 8]:
            print("Jam lembur tidak sesuai ketentuan!")
            print("Silakan masukkan ulang.")

        else:
            break

    # Menghitung upah lembur
    if 1 <= lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    # Input shift malam
    while True:
        shift = input("Apakah shift malam? (y/n): ").lower()

        if shift == "y" or shift == "n":
            break
        else:
            print("Input tidak valid! Masukkan y atau n.")

    # Menghitung tambahan shift malam
    if shift == "y":
        upah_shift = bonus_malam
    else:
        upah_shift = 0

    # Menghitung gaji harian
    gaji_harian = gaji_pokok + upah_lembur + upah_shift

    # Menambahkan gaji harian ke total gaji
    total_gaji += gaji_harian

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}")

# Menampilkan total gaji mingguan
print("\n=== HASIL GAJI MINGGUAN ===")
print(f"Total gaji selama 7 hari: Rp{total_gaji:,}")
