totalGaji = 0
gajiPokok = 100000

for hari in range(1, 8):
    print(f"\nhari ke-{hari}")

    while True:
        lembur = int(input("masukkan jam lembur: "))

        if lembur < 0:
            print("jam lembur tidak boleh negatif.")
        elif lembur > 8:
            print("jumlah lembur melebihi batas yang ditentukan.")
            print("upah lembur tidak dihitung.")
            break
        elif lembur in [0, 1, 2, 3, 4, 6, 8]:
            break
        else:
            print("jam lembur tidak sesuai ketentuan.")
            print("silakan masukkan ulang.")

    if lembur in [1, 2, 3]:
        upahLembur = lembur * 25000
    elif lembur == 4:
        upahLembur = 100000
    elif lembur == 6:
        upahLembur = 200000
    elif lembur == 8:
        upahLembur = 300000
    else:
        upahLembur = 0

    shift = input("bekerja shift malam? (ya/tidak): ")

    if shift == "ya":
        tambahanShift = 50000
    else:
        tambahanShift = 0

    gajiHarian = gajiPokok + upahLembur + tambahanShift
    totalGaji += gajiHarian

    print(f"gaji hari ini: Rp{gajiHarian:,}")

print(f"\ntotal gaji mingguan: Rp{totalGaji:,}")
