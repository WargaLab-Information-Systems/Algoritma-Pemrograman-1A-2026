total_gaji = 0
GAJI_POKOK = 100000
TAMBAHAN_SHIFT_MALAM = 50000

for hari in range(1, 8):
    print("Hari ke-", hari, "---")

    while True:
        jam = input("Masukkan jam lembur (0 - 8 jam): ")
        if jam == "":
            print("Input tidak boleh kosong!")
        elif jam.startswith("-") and jam[1:].isdigit():
            print("Jam lembur tidak boleh negatif!")
        elif not jam.isdigit():
            print("Input wajib berupa angka!")
        elif int(jam) > 8:
            print("Pesan: Jumlah lembur melebihi batas maksimal (8 jam). Silakan masukkan ulang!")
        else:
            jam = int(jam)
            break

    while True:
        shift = input("Apakah bekerja pada shift malam? (y/n): ").lower()
        if shift == "y" or shift == "n":
            break
        print("Masukkan y untuk ya atau n untuk tidak!")

    if jam == 4:
        lembur = 100000
    elif jam == 6:
        lembur = 200000
    elif jam == 8:
        lembur = 300000
    else:
        lembur = jam * 25000

    if shift == "y":
        bonus = TAMBAHAN_SHIFT_MALAM
    else:
        bonus = 0

    gaji_harian = GAJI_POKOK + lembur + bonus
    total_gaji = total_gaji + gaji_harian

    print("Gaji Hari ke-", hari, ": Rp", gaji_harian)
print("TOTAL GAJI MINGGUAN KARYAWAN: Rp", total_gaji)
