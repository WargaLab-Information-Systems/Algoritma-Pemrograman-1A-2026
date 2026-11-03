
total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    jam_lembur = int(input("Masukkan jam lembur: "))

    while jam_lembur < 0 or jam_lembur == 5 or jam_lembur == 7 or jam_lembur > 8:
        print("Jam lembur tidak sesuai ketentuan!")
        jam_lembur = int(input("Masukkan ulang jam lembur: "))

    gaji = 100000

    if jam_lembur >= 1 and jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Bekerja shift malam? (y/t): ")

    if shift == "y":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    gaji_harian = gaji + upah_lembur + tambahan_shift
    total_gaji += gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("Total gaji mingguan: Rp", total_gaji)
