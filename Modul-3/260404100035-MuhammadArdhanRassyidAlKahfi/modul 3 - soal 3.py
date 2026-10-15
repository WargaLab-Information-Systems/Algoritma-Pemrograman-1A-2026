jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0
nilai_tertinggi = 0
nilai_terendah = 100
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print("Mahasiswa ke-", i)

    # Input nama dengan validasi
    while True:
        nama = input("Masukkan nama mahasiswa: ")

        if nama.strip() == "":
            print("Nama tidak boleh kosong! Silakan masukkan nama mahasiswa.")
        elif not any(huruf.isalpha() for huruf in nama):
            print("Nama harus berupa huruf, bukan angka!")
        else:
            break

    # Input nilai tugas dengan validasi
    while True:
        try:
            input_tugas = input("Masukkan nilai tugas: ")

            if input_tugas.strip() == "":
                print("Nilai tugas tidak boleh kosong!")
                continue

            tugas = float(input_tugas)

            if tugas < 0 or tugas > 100:
                print("Nilai tugas harus berada antara 0 sampai 100!")
                continue

            break
        except ValueError:
            print("Input harus berupa angka, bukan teks atau kalimat!")

    # Input nilai UTS dengan validasi
    while True:
        try:
            input_uts = input("Masukkan nilai UTS: ")

            if input_uts.strip() == "":
                print("Nilai UTS tidak boleh kosong!")
                continue

            uts = float(input_uts)

            if uts < 0 or uts > 100:
                print("Nilai UTS harus berada antara 0 sampai 100!")
                continue

            break
        except ValueError:
            print("Input harus berupa angka, bukan teks atau kalimat!")

    # Input nilai UAS dengan validasi
    while True:
        try:
            input_uas = input("Masukkan nilai UAS: ")

            if input_uas.strip() == "":
                print("Nilai UAS tidak boleh kosong!")
                continue

            uas = float(input_uas)

            if uas < 0 or uas > 100:
                print("Nilai UAS harus berada antara 0 sampai 100!")
                continue

            break
        except ValueError:
            print("Input harus berupa angka, bukan teks atau kalimat!")

    nilai_akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("Nama:", nama)
    print("Nilai tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("Nilai akhir:", nilai_akhir)
    print("Kategori:", kategori)

    total_nilai += nilai_akhir

    if i == 1:
        nilai_tertinggi = nilai_akhir
        nilai_terendah = nilai_akhir
        nama_tertinggi = nama
        nama_terendah = nama
    else:
        if nilai_akhir > nilai_tertinggi:
            nilai_tertinggi = nilai_akhir
            nama_tertinggi = nama

        if nilai_akhir < nilai_terendah:
            nilai_terendah = nilai_akhir
            nama_terendah = nama

rata_rata = total_nilai / 10

print("REKAP NILAI MAHASISWA")
print("Jumlah kategori A:", jumlah_A)
print("Jumlah kategori B:", jumlah_B)
print("Jumlah kategori C:", jumlah_C)
print("Jumlah kategori D:", jumlah_D)
print("Jumlah kategori E:", jumlah_E)

print("Nilai akhir tertinggi:", nilai_tertinggi)
print("Nama mahasiswa:", nama_tertinggi)

print("Nilai akhir terendah:", nilai_terendah)
print("Nama mahasiswa:", nama_terendah)

print("Rata-rata nilai akhir:", rata_rata)