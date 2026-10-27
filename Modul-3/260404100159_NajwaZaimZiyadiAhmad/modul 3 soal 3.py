
print("=== PROGRAM NILAI MAHASISWA ===")

jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai_akhir = 0
nilai_tertinggi = -1
nilai_terendah = 101

nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print(f"\nData mahasiswa ke-{i}")

    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    # Menghitung nilai akhir
    nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

    # Menentukan kategori nilai
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

    total_nilai_akhir += nilai_akhir

    # Mencari nilai tertinggi
    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    # Mencari nilai terendah
    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

    print("\nHasil nilai mahasiswa:")
    print("Nama:", nama)
    print("Nilai tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print(f"Nilai akhir: {nilai_akhir:.2f}")
    print("Kategori:", kategori)

# Menghitung rata-rata kelas
rata_rata = total_nilai_akhir / 10

print("\n=== REKAPITULASI NILAI KELAS ===")
print("Jumlah mahasiswa kategori A:", jumlah_A)
print("Jumlah mahasiswa kategori B:", jumlah_B)
print("Jumlah mahasiswa kategori C:", jumlah_C)
print("Jumlah mahasiswa kategori D:", jumlah_D)
print("Jumlah mahasiswa kategori E:", jumlah_E)

print("\nNilai akhir tertinggi:", nilai_tertinggi)
print("Mahasiswa:", nama_tertinggi)

print("\nNilai akhir terendah:", nilai_terendah)
print("Mahasiswa:", nama_terendah)

print(f"\nRata-rata nilai akhir kelas: {rata_rata:.2f}")
