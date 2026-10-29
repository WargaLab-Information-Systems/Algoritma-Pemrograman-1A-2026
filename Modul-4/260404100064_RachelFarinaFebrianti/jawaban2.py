totalGaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    gajiPokok = 100000

    while True:
        jamLembur = int(input("Masukkan jam lembur: "))

        if jamLembur < 0:
            print("Jam lembur tidak boleh negatif, masukkan ulang!")
        elif jamLembur == 5 or jamLembur == 7:
            print("Jam lembur tidak sesuai ketentuan, masukkan ulang!")
        else:
            break

    if jamLembur >= 1 and jamLembur <= 3:
        upahLembur = jamLembur * 25000
    elif jamLembur == 4:
        upahLembur = 100000
    elif jamLembur == 6:
        upahLembur = 200000
    elif jamLembur == 8:
        upahLembur = 300000
    elif jamLembur > 8:
        print("Jumlah lembur melebihi batas yang ditentukan!")
        upahLembur = 0
    else:
        upahLembur = 0

    shiftMalam = input("Bekerja shift malam? (ya/tidak): ")

    if shiftMalam == "ya":
        tambahanShift = 50000
    else:
        tambahanShift = 0

    gajiHarian = gajiPokok + upahLembur + tambahanShift
    totalGaji = totalGaji + gajiHarian

    print("Gaji hari ini: Rp", gajiHarian)

print("Total gaji mingguan: Rp", totalGaji)