# Program Gaji Mingguan Karyawan - Pak Rudi

total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    # Validasi jam lembur
    lembur = int(input("Jam lembur: "))
    while lembur < 0 or lembur == 5 or lembur == 7:
        print("Jam lembur tidak sesuai, masukkan ulang!")
        lembur = int(input("Jam lembur: "))

    shift = input("Shift malam? (y/t): ")

    # Hitung upah lembur
    if lembur == 0:
        upah_lembur = 0
    elif lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        print("Jumlah lembur melebihi batas yang ditentukan")
        upah_lembur = 0

    # Hitung gaji hari ini
    gaji = 100000 + upah_lembur
    if shift == "y":
        gaji = gaji + 50000

    total_gaji = total_gaji + gaji
    print("Gaji hari ini: Rp", gaji)
    print()

print("Total gaji mingguan: Rp", total_gaji)