def hitungNilai(nama, tugas, uts, uas):
    nilaiAkhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilaiAkhir >= 85:
        grade = "A"
        status = "lulus"
    elif nilaiAkhir >= 70:
        grade = "B"
        status = "lulus"
    elif nilaiAkhir >= 55:
        grade = "C"
        status = "lulus"
    else:
        grade = "D"
        status = "tidak lulus"

    print("\n===== HASIL NILAI MAHASISWA =====")
    print("nama mahasiswa :", nama)
    print("nilai tugas     :", tugas)
    print("nilai UTS       :", uts)
    print("nilai UAS       :", uas)
    print("nilai akhir     :", nilaiAkhir)
    print("grade           :", grade)
    print("status          :", status)

nama = input("masukkan nama mahasiswa: ")
tugas = float(input("masukkan nilai tugas: "))
uts = float(input("masukkan nilai UTS: "))
uas = float(input("masukkan nilai UAS: "))

hitungNilai(nama, tugas, uts, uas)
