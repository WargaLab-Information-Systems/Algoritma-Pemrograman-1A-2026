def nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("HASIL NILAI MAHASISWA")
    print("Nama mahasiswa:", nama)
    print("Nilai tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("Nilai akhir:", nilai_akhir)
    print("Grade:", grade)
    print("Status:", status)

nama = str(input("Masukkan nama mahasiswa: ")) 
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_mahasiswa(nama, tugas, uts, uas)