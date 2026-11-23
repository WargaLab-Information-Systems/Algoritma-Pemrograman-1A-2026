# Membuat fungsi
def hitung_nilai(nama, tugas, uts, uas):
    nilai = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai >= 85:
        predikat = "A"
    elif nilai >= 70:
        predikat = "B"
    elif nilai >= 55:
        predikat = "C"
    else: 
        predikat = "D" 

    if predikat == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("Nama:", nama)
    print("Nilai Akhir:", nilai)
    print("Predikat:", predikat)
    print("Status:", status)

# Input data
nama = input("Masukkan nama: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Memanggil fungsi
hitung_nilai(nama, tugas, uts, uas)