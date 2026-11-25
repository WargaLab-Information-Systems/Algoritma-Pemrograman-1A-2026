def hitungNilai(tugas, uts, uas):
    total = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if total >= 85:
        grade = "A"
    elif total >= 70:
        grade = "B"
    elif total >= 55:
        grade = "C"
    else:
        grade = "D"

    print()
    print(f"Nilai Akhir: {total:.2f}")
    print(f"Grade Mahasiswa: {grade}")
    status = print("Tidak Lulus") if grade == "D" else print("Lulus")

nilaiTugas = input("Masukkan nilai tugas: ")
while not(nilaiTugas.isdigit()):
    print("Data tidak valid!")
    nilaiTugas = input("Masukkan nilai tugas: ")
nilaiTugas = int(nilaiTugas)

if nilaiTugas > 100:
    while not(nilaiTugas.isdigit()):
        print("Data tidak valid!")
        nilaiTugas = input("Masukkan nilai tugas: ")
    nilaiTugas = int(nilaiTugas)

nilaiUTS = input("Masukkan nilai UTS: ")
while not(nilaiUTS.isdigit()):
    print("Data tidak valid!")
    nilaiUTS = input("Masukkan nilai tugas: ")
nilaiUTS = int(nilaiUTS)

nilaiUAS = input("Masukkan nilai UAS: ")
while not(nilaiUAS.isdigit()):
    print("Data tidak valid!")
    nilaiUAS = input("Masukkan nilai tugas: ")
nilaiUAS = int(nilaiUAS)

hitungNilai(nilaiTugas, nilaiUTS, nilaiUAS)
