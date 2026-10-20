jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0
nilai_tertinggi = 0
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print("\n=== Mahasiswa ke-", i, "===")

    nama = input("Nama: ")
    while True:
        tugas = float(input("Nilai Tugas: "))
        if tugas >= 0 and tugas <= 100:
            break
        else:
            print("Nilai Tugas harus antara 0-100, ulangi.")
    while True:
        uts = float(input("Nilai UTS: "))
        if uts >= 0 and uts <= 100:
            break
        else:
            print("Nilai UTS harus antara 0-100, ulangi.")
    while True:
        uas = float(input("Nilai UAS: "))
        if uas >= 0 and uas <= 100:
            break
        else:
            print("Nilai UAS harus antara 0-100, ulangi.")

    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("\n--- Hasil Nilai ---")
    print("Nama:", nama)
    print("Nilai tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("Nilai akhir:", round(akhir, 2))
    print("Kategori:", kategori)

    total_nilai += akhir

    if i == 1:
        nilai_tertinggi = akhir
        nilai_terendah = akhir
        nama_tertinggi = nama
        nama_terendah = nama
    else:
        if akhir > nilai_tertinggi:
            nilai_tertinggi = akhir
            nama_tertinggi = nama

        if akhir < nilai_terendah:
            nilai_terendah = akhir
            nama_terendah = nama

print("\n===== REKAP KELAS =====")
print("Jumlah kategori A:", jumlah_A)
print("Jumlah kategori B:", jumlah_B)
print("Jumlah kategori C:", jumlah_C)
print("Jumlah kategori D:", jumlah_D)
print("Jumlah kategori E:", jumlah_E)

print("Nilai tertinggi:", nama_tertinggi, round(nilai_tertinggi, 2))
print("Nilai terendah:", nama_terendah, round(nilai_terendah, 2))
print("Rata-rata nilai akhir:", round(total_nilai / 10, 2))