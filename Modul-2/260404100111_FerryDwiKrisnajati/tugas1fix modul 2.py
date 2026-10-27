kode = int(input("Masukkan kode rahasia 3 digit: "))
digit1 = kode //100
digit2 = (kode // 10) % 10
digit3 = kode % 10
pelacak = digit1 * digit3
if digit2 % 2 == 1:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - digit2
pelacak_tahap1 = pelacak
if pelacak % 3 == 0:
    pelacak = pelacak // 3
else:
    pelacak = pelacak * 2
nilai_akhir = pelacak
if nilai_akhir > 50:
    status = "Kategori A"
elif nilai_akhir > 20:
    status = "Kategori B"
else:
    status = "sKrasny Ditolak"
if nilai_akhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"
print("== HASIL PEMERIKSAAN ==")
print("Digit pertama :", digit1)
print("Digit kedua :", digit2)
print("Digit ketiga :", digit3)
print("Nilai pelacak awal :", digit1 * digit3)
print("Nilai pelacak setelah tahap 1 :", pelacak_tahap1)
print("Nilai pelacak setelah tahap 2 :", nilai_akhir)
print("Status sKrasny :", status)
print("Siklus :", siklus)