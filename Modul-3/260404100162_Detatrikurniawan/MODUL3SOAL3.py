mahasisawa = True
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0
nilai_tertinggi = -1
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

while True:
    print(f"\nMahasiswa ke {mahasisawa}")
    nama = input("Nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

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

    total_nilai += akhir

    if akhir > nilai_tertinggi:
        nilai_tertinggi = akhir
        nama_tertinggi = nama
    if akhir < nilai_terendah:
        nilai_terendah = akhir
        nama_terendah = nama

    print(f"Nama: {nama} | Tugas: {tugas:.0f} | UTS: {uts:.0f} | UAS: {uas:.0f} | Akhir: {akhir:.2f} | Kategori: {kategori}")

print("\nREKAP")
print("Jumlah kategori A :", jumlah_A)
print("Jumlah kategori B :", jumlah_B)
print("Jumlah kategori C :", jumlah_C)
print("Jumlah kategori D :", jumlah_D)
print("Jumlah kategori E :", jumlah_E)
print(f"Nilai tertinggi: {nilai_tertinggi:.2f} ({nama_tertinggi})")
print(f"Nilai terendah: {nilai_terendah:.2f} ({nama_terendah})")
print(f"Rata-rata nilai: {total_nilai / 10:.2f}")