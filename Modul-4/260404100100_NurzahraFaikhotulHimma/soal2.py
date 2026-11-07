total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    lembur = int(input("Masukkan jam lembur (0, 1-4, 6, atau 8): "))

    while lembur < 0 or lembur > 8 or lembur == 5 or lembur == 7:
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    gaji = 100000

    if lembur >= 1 and lembur <= 3:
        gaji_lembur = lembur * 25000
    elif lembur == 4:
        gaji_lembur = 100000
    elif lembur == 6:
        gaji_lembur = 200000
    elif lembur == 8:
        gaji_lembur = 300000
    else:
        gaji_lembur = 0

    shift = input("Bekerja shift malam? (ya/tidak): ")

    if shift == "ya":
        gaji = gaji + 50000

    gaji = gaji + gaji_lembur
    total_gaji = total_gaji + gaji

    print("Gaji hari ke-", hari, "adalah Rp", gaji)

print("\nTotal gaji selama seminggu: Rp", total_gaji)