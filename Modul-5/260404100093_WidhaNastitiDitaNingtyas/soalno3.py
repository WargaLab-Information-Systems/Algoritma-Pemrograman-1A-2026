def nilai_mahasiswa(nama, tugas, uts, uas):
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print("\n=== HASIL NILAI MAHASISWA ===")
    print("Nama Mahasiswa  :", nama)
    print("Nilai Tugas     :", tugas)
    print("Nilai UTS       :", uts)
    print("Nilai UAS       :", uas)
    print("Nilai Akhir     :", akhir)
    print("Grade           :", grade)
    print("Status          :", status)


nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
while tugas > 100:
    print("nilai tidak valid")
    tugas = float(input("Masukkan nilai tugas ulang: "))

uts = float(input("Masukkan nilai UTS: "))
while uts > 100:
    print("nilai tidak valid")
    uts = float(input("Masukkan nilai uts ulang: "))

uas = float(input("Masukkan nilai UAS: "))
while uas > 100:
    print("nilai tidak valid")
    uas = float(input("Masukkan nilai uas ulang: "))

nilai_mahasiswa(nama, tugas, uts, uas)