
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0

for i in range(1, 11):
    print("Mahasiswa ke-", i)

    nama = str(input("Masukkan nama: "))
    tugas = int(input("Masukkan nilai tugas: "))
    uts = int(input("Masukkan nilai UTS: "))
    uas = int(input("Masukkan nilai UAS: "))

    nilai_tugas = tugas * 30 / 100
    nilai_uts = uts * 30 / 100
    nilai_uas = uas * 40 / 100

    nilai_akhir = nilai_tugas + nilai_uts + nilai_uas

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A = jumlah_A + 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B = jumlah_B + 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C = jumlah_C + 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D = jumlah_D + 1
    else:
        kategori = "E"
        jumlah_E = jumlah_E + 1

    print("Nama:", nama)
    print("Nilai tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("Nilai akhir:", nilai_akhir)
    print("Kategori:", kategori)

    total_nilai = total_nilai + nilai_akhir

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

print("REKAPITULASI NILAI MAHASISWA")
print("Jumlah kategori A:", jumlah_A)
print("Jumlah kategori B:", jumlah_B)
print("Jumlah kategori C:", jumlah_C)
print("Jumlah kategori D:", jumlah_D)
print("Jumlah kategori E:", jumlah_E)
print("Nilai tertinggi:", nilai_tertinggi)
print("Nama mahasiswa:", nama_tertinggi)
print("Nilai terendah:", nilai_terendah)
print("Nama mahasiswa:", nama_terendah)
print("Rata-rata nilai akhir:", rata_rata)

