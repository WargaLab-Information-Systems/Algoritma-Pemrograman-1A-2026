def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai_akhir >= 85:
        grade = "A"
        keterangan = "Lulus"
    elif nilai_akhir >= 70:
        grade = "B"
        keterangan = "Lulus"
    elif nilai_akhir >= 55:
        grade = "C"
        keterangan = "Lulus"
    else:
        grade = "D"
        keterangan = "Tidak Lulus"

    print("\n===== HASIL PENILAIAN =====")
    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", nilai_akhir)
    print("Grade          :", grade)
    print("Keterangan     :", keterangan)


nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))


hitung_nilai(nama, tugas, uts, uas)