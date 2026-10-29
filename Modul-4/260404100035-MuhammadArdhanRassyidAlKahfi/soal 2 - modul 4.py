total_gaji = 0
total_lembur = 0
total_shift = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    while True:
        teks = input("Masukkan jam lembur: ").strip()

        if teks == "":
            print("Input tidak boleh kosong!")
        elif not teks.isdigit():
            print("Input harus berupa bilangan bulat!")
        elif int(teks) in (5, 7):
            print("Ketentuan upah untuk jam tersebut tidak tersedia. Masukkan ulang!")
        else:
            jam_lembur = int(teks)
            break

    if jam_lembur == 0:
        upah_lembur = 0
    elif jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        print("Jumlah lembur melebihi 8 jam.")
        print("Upah lembur hari ini tidak dihitung.")
        upah_lembur = 0

    while True:
        shift = input("Apakah bekerja shift malam? (ya/tidak): ").strip().lower()

        if shift == "":
            print("Input tidak boleh kosong!")
        elif shift == "ya" or shift == "tidak":
            break
        else:
            print("Input tidak valid! Masukkan ya atau tidak.")

    if shift == "ya":
        upah_shift = 50000
    else:
        upah_shift = 0

    gaji_harian = 100000 + upah_lembur + upah_shift

    total_gaji += gaji_harian
    total_lembur += upah_lembur
    total_shift += upah_shift

    print(f"Gaji pokok: Rp{100000}")
    print(f"Upah lembur: Rp{upah_lembur}")
    print(f"Tambahan shift: Rp{upah_shift}")
    print(f"Gaji harian: Rp{gaji_harian}")

print("\nREKAP GAJI MINGGUAN ")
print(f"Total gaji pokok: Rp{700000}")
print(f"Total upah lembur: Rp{total_lembur}")
print(f"Total tambahan shift: Rp{total_shift}")
print(f"Total gaji mingguan: Rp{total_gaji}")