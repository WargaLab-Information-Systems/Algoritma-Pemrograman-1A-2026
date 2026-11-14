# yg harus d tampilkan
jumlahA = 0
jumlahB = 0
jumlahC = 0
jumlahD = 0
jumlahE = 0

totalNilaiAkhir = 0
nilaiTertinggi = -1
nilaiTerendah = 101
namaTertinggi = ""
namaTerendah = ""

for i in range(1, 11):
    print("mahasiswa ke-", i)

    nama = input("masukkan nama mahasiswa: ")
    tugas = float(input("masukkan nilai tugas: "))
    uts = float(input("masukkan nilai UTS: "))
    uas = float(input("masukkan nilai UAS: "))

    nilaiAkhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilaiAkhir >= 85:
        kategori = "A"
        jumlahA += 1
    elif nilaiAkhir >= 75:
        kategori = "B"
        jumlahB += 1
    elif nilaiAkhir >= 65:
        kategori = "C"
        jumlahC += 1
    elif nilaiAkhir >= 50:
        kategori = "D"
        jumlahD += 1
    else:
        kategori = "E"
        jumlahE += 1

    print("nama:", nama)
    print("nilai tugas:", tugas)
    print("nilai UTS:", uts)
    print("nilai UAS:", uas)
    print("nilai akhir:", nilaiAkhir)
    print("kategori nilai:", kategori)

    totalNilaiAkhir += nilaiAkhir

    if nilaiAkhir > nilaiTertinggi:
        nilaiTertinggi = nilaiAkhir
        namaTertinggi = nama

    if nilaiAkhir < nilaiTerendah:
        nilaiTerendah = nilaiAkhir
        namaTerendah = nama

rataRata = totalNilaiAkhir / 10

print("=== REKAP NILAI MAHASISWA ===")
print("Jumlah mahasiswa kategori A:", jumlahA)
print("Jumlah mahasiswa kategori B:", jumlahB)
print("Jumlah mahasiswa kategori C:", jumlahC)
print("Jumlah mahasiswa kategori D:", jumlahD)
print("Jumlah mahasiswa kategori E:", jumlahE)
print("Nilai tertinggi:", nilaiTertinggi, "-", namaTertinggi)
print("Nilai terendah:", nilaiTerendah, "-", namaTerendah)
print("Rata-rata nilai akhir:", rataRata)
