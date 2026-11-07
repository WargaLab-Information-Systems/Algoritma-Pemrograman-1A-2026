def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        grade = "A"
        status = "Lulus"
    elif nilai_akhir >= 70:
        grade = "B"
        status = "Lulus"
    elif nilai_akhir >= 55:
        grade = "C"
        status = "Lulus"
    else:
        grade = "D"
        status = "Tidak Lulus"

    print("\n HASIL PERHITUNGAN NILAI ")
    print(f"Nama mahasiswa: {nama}")
    print(f"Nilai tugas: {tugas}")
    print(f"Nilai UTS: {uts}")
    print(f"Nilai UAS: {uas}")
    print(f"Nilai akhir: {nilai_akhir:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")

while True:
    nama = input("Masukkan nama mahasiswa: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong!")
    elif not nama.replace(" ", "").isalpha():
        print("Nama harus berupa huruf, bukan angka atau simbol!")
    else:
        break

while True:
    teks = input("Masukkan nilai tugas: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isdigit():
        print("Input harus berupa angka!")
    elif int(teks) > 100:
        print("Nilai tidak boleh lebih dari 100!")
    else:
        tugas = int(teks)
        break

while True:
    teks = input("Masukkan nilai UTS: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isdigit():
        print("Input harus berupa angka!")
    elif int(teks) > 100:
        print("Nilai tidak boleh lebih dari 100!")
    else:
        uts = int(teks)
        break

while True:
    teks = input("Masukkan nilai UAS: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isdigit():
        print("Input harus berupa angka!")
    elif int(teks) > 100:
        print("Nilai tidak boleh lebih dari 100!")
    else:
        uas = int(teks)
        break

hitung_nilai(nama, tugas, uts, uas)
