
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total = 0
tertinggi = -1
terendah = 101

for i in range(1, 11):
    print("Mahasiswa ke-", i)

    nama = input("Nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

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

    print("Nama:", nama)
    print("Nilai akhir:", akhir)
    print("Kategori:", kategori)

    total = total + akhir

    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama

    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("Jumlah kategori A:", jumlah_A)
print("Jumlah kategori B:", jumlah_B)
print("Jumlah kategori C:", jumlah_C)
print("Jumlah kategori D:", jumlah_D)
print("Jumlah kategori E:", jumlah_E)

print("Nilai tertinggi:", tertinggi)
print("Nama nilai tertinggi:", nama_tertinggi)

print("Nilai terendah:", terendah)
print("Nama nilai terendah:", nama_terendah)

print("Rata-rata kelas:", total / 10)