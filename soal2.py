GAJI_POKOK = 100000
BONUS_MALAM = 50000
total_gaji = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    # Validasi jam lembur
    while True:
        jam = int(input("Masukkan jam lembur: "))
        if jam < 0 or jam in (5, 7):
            print("Jam lembur tidak sesuai ketentuan. Silakan ulangi.")
        else:
            break

    # Validasi shift malam
    while True:
        shift = input("Shift malam? (iya/tidak): ").lower()
        if shift in ("iya", "tidak"):
            break
        print("Masukkan 'iya' atau 'tidak'. Silakan ulangi.")

    # Menentukan upah lembur
    if jam == 0:
        upah_lembur = 0
    elif 1 <= jam <= 3:
        upah_lembur = jam * 25000
    elif jam == 4:
        upah_lembur = 100000
    elif jam == 6:
        upah_lembur = 200000
    elif jam == 8:
        upah_lembur = 300000
    else:  # jam > 8
        print("Jumlah lembur melebihi batas yang ditentukan. Upah lembur tidak dihitung.")
        upah_lembur = 0

    upah_malam = BONUS_MALAM if shift == "iya" else 0
    gaji_hari_ini = GAJI_POKOK + upah_lembur + upah_malam
    total_gaji += gaji_hari_ini
    print(f"Gaji hari ke-{hari}: Rp{gaji_hari_ini:,}")

print(f"\nTotal gaji mingguan: Rp{total_gaji:,}")