total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    jam_lembur = int(input("Masukkan jam lembur: "))

    while jam_lembur not in [0, 1, 2, 3, 4, 6, 8]:
        if jam_lembur > 8:
            print("Jam lembur melebihi batas yang ditentukan.")
            break
        else:
            print("Jam lembur tidak sesuai ketentuan.")
            jam_lembur = int(input("Masukkan ulang jam lembur: "))

    gaji_harian = 100000
    upah_lembur = 0

    if jam_lembur == 1 or jam_lembur == 2 or jam_lembur == 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000

    shift_malam = input("Bekerja shift malam? (ya/tidak): ")

    if shift_malam == "ya":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    gaji_harian = gaji_harian + upah_lembur + tambahan_shift
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("\nTotal gaji mingguan: Rp", total_gaji)
