# Membuat fungsi untuk menghitung nilai akhir mahasiswa
def hitung_nilai(nama, tugas, uts, uas):

    # Menghitung nilai akhir berdasarkan bobot yang ditentukan
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    # Menentukan grade berdasarkan nilai akhir
    if nilai_akhir >= 85:
        grade = "A"

    # Jika nilai akhir minimal 70
    elif nilai_akhir >= 70:
        grade = "B"

    # Jika nilai akhir minimal 55
    elif nilai_akhir >= 55:
        grade = "C"

    # Jika nilai akhir kurang dari 55
    else:
        grade = "D"

    # Menentukan status kelulusan mahasiswa
    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"

    # Jika mahasiswa mendapatkan grade D
    else:
        status = "Tidak Lulus"

    # Menampilkan hasil perhitungan mahasiswa

    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", round(nilai_akhir, 2))
    print("Grade          :", grade)
    print("Status         :", status)


# Meminta pengguna memasukkan nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Meminta pengguna memasukkan nilai tugas
tugas = float(input("Masukkan nilai tugas: "))

# Meminta pengguna memasukkan nilai UTS
uts = float(input("Masukkan nilai UTS: "))

# Meminta pengguna memasukkan nilai UAS
uas = float(input("Masukkan nilai UAS: "))

# Memanggil fungsi untuk menghitung dan menampilkan nilai
hitung_nilai(nama, tugas, uts, uas)