total_gaji = 0  # variabel akumulator

for hari in range(1, 8):
    print("Hari ke-", hari)
    gaji_hari = 100000  # gaji pokok per hari

    # Validasi jam lembur (diulang sampai input sesuai ketentuan)
    while True:
        jam_str = input("Jam lembur: ")
        if not jam_str:
            print("Masukan Tidak Boleh Kosong")
            continue
        if jam_str[0] == "-":
            print("Masukan Tidak Boleh Minus")
            continue
        jam_int = True
        for karakter in jam_str:
            if karakter not in '0987654321':
                jam_int = False
                break
        if not jam_int:
            print("Masukan Tidak Boleh Selain Angka")
            continue
        jam = int(jam_str)
        if jam <= 0:
            print("Angka Tidak Boleh Minus dan 0")
            continue
        if jam < 0 or jam == 5 or jam == 7:
            print("Jam lembur tidak sesuai ketentuan, silakan ulangi.")
            continue
        else:
            break

    # Menentukan upah lembur
    if jam == 0:
        upah_lembur = 0
    elif jam >= 1 and jam <= 3:
        upah_lembur = jam * 25000
    elif jam == 4:
        upah_lembur = 100000
    elif jam == 6:
        upah_lembur = 200000
    elif jam == 8:
        upah_lembur = 300000
    else:
        print("Jumlah lembur melebihi batas yang ditentukan.")
        upah_lembur = 0

    gaji_hari = gaji_hari + upah_lembur

    # Validasi shift malam
    while True:
        shift = input("Shift malam? (y/t): ")
        if shift == "y" or shift == "t":
            break
        print("Ketik y atau t saja, silakan ulangi.")

    if shift == "y":
        gaji_hari = gaji_hari + 50000

    print("Gaji hari ke-", hari, ": Rp", gaji_hari)
    print()
    total_gaji = total_gaji + gaji_hari

print("Total gaji mingguan: Rp", total_gaji)