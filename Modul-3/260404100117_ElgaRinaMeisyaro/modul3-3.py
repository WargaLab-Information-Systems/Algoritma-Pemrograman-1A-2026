mahasiswa = []
jumlah_nilai = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
total_nilai = 0

for i in range(10):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai_akhir >= 85:
        kategori = "A"
    elif nilai_akhir >= 75:
        kategori = "B"
    elif nilai_akhir >= 65:
        kategori = "C"
    elif nilai_akhir >= 50:
        kategori = "D"
    else:
        kategori = "E"

    mahasiswa.append([nama, tugas, uts, uas, nilai_akhir, kategori])
    jumlah_nilai[kategori] += 1
    total_nilai += nilai_akhir

print("\n========== DATA NILAI MAHASISWA ==========")

for m in mahasiswa:
    print("\nNama:", m[0])
    print("Nilai Tugas:", m[1])
    print("Nilai UTS:", m[2])
    print("Nilai UAS:", m[3])
    print("Nilai Akhir:", round(m[4], 2))
    print("Kategori:", m[5])

print("\n========== REKAPITULASI NILAI ==========")

print("Jumlah mahasiswa kategori A:", jumlah_nilai["A"])
print("Jumlah mahasiswa kategori B:", jumlah_nilai["B"])
print("Jumlah mahasiswa kategori C:", jumlah_nilai["C"])
print("Jumlah mahasiswa kategori D:", jumlah_nilai["D"])
print("Jumlah mahasiswa kategori E:", jumlah_nilai["E"])

tertinggi = max(mahasiswa, key=lambda m: m[4])
terendah = min(mahasiswa, key=lambda m: m[4])
rata_rata = total_nilai / 10

print("\nNilai akhir tertinggi:", round(tertinggi[4], 2))
print("Nama mahasiswa:", tertinggi[0])

print("\nNilai akhir terendah:", round(terendah[4], 2))
print("Nama mahasiswa:", terendah[0])

print("\nRata-rata nilai akhir:", round(rata_rata, 2))