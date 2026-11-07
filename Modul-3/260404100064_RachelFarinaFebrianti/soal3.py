jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_akhir = 0
tertinggi = -1
terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print("Mahasiswa ke-", i)
    nama = input("Masukkan nama: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    akhir = tugas * 30 / 100 + uts * 30 / 100 + uas * 40 / 100
    if akhir >= 85:
        kategori = "A"
        jumlah_A = jumlah_A + 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B = jumlah_B + 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C = jumlah_C + 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D = jumlah_D + 1
    else:
        kategori = "E"
        jumlah_E = jumlah_E + 1
    print("Nama :", nama)
    print("Nilai tugas :", tugas)
    print("Nilai UTS :", uts)
    print("Nilai UAS :", uas)
    print("Nilai akhir :", akhir)
    print("Kategori :", kategori)
    total_akhir = total_akhir + akhir
    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

rata = total_akhir / 10
print("Jumlah kategori A :", jumlah_A)
print("Jumlah kategori B :", jumlah_B)
print("Jumlah kategori C :", jumlah_C)
print("Jumlah kategori D :", jumlah_D)
print("Jumlah kategori E :", jumlah_E)
print("Nilai tertinggi :", tertinggi, "oleh", nama_tertinggi)
print("Nilai terendah :", terendah, "oleh", nama_terendah)
print("Rata-rata nilai akhir :", rata)
