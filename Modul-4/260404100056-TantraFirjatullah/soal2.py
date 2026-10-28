gaji = 0
for i in range(7):
    print()
    print(f"Masukkan data hari ke-{i+1}")
    statusKerja = input("Apakah bekerja pada hari tersebut?(y/n): ").lower()
    while not(statusKerja == "y" or statusKerja == "n"):
        print("Masukan tidak valid!")
        print()
        statusKerja = input("Apakah bekerja pada hari tersebut?(y/n): ").lower()

    if statusKerja == "y":
        shiftMalam = input("Melakukan shift malam?(y/n): ").lower()
        while not(shiftMalam == "y" or shiftMalam == "n"):
            print("Masukan tidak valid!")
            print()
            shiftMalam = input("Melakukan shift malam?(y/n): ").lower()

        jamLembur = input("Lama jam lembur: ")
        while not(jamLembur.isdigit()):
            print("Masukan tidak valid!")
            print()
            jamLembur = input("Lama jam lembur: ")

        jamLembur = int(jamLembur)
        upahLembur = (jamLembur * 25000) if jamLembur <= 3 else 100000 if jamLembur < 6 else 200000 if jamLembur < 8 else 300000 if jamLembur == 8 else 0

        if jamLembur > 8:
            print("Upah tidak didapat, overwork tidak baik!")

        upahMalam = 50000 if shiftMalam == "y" else 0
        gaji += 100000 + (upahLembur + upahMalam)
    else:
        gaji += 0

print()
print(f"Gaji Minggu Ini: Rp{gaji}")
