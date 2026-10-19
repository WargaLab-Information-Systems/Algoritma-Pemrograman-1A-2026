print("===== System Krasny =====")
print("Masukkan kode rahasia 3 digit:")
kode = int(input())
digit1 = float(kode) / 100
digit2 = float(kode) / 10 % 10
digit3 = kode % 10
pelacak = digit1 * digit3
if digit2 % 2 != 0:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - digit2
tahap1 = pelacak
if pelacak % 3 == 0:
    nilaiAkhir = float(pelacak) / 3
else:
    nilaiAkhir = pelacak * 2
if nilaiAkhir > 50:
    status = "Kategori A"
else:
    if nilaiAkhir > 20:
        status = "Kategori B"
    else:
        status = "sKrasny Ditolak"
if nilaiAkhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"
print("Digit pertama = " + str(digit1))
print("Digit kedua = " + str(digit2))
print("Digit ketiga = " + str(digit3))
print("Nilai pelacak awal = " + str(digit1 * digit3))
print("Nilai pelacak setelah tahap pertama = " + str(tahap1))
print("Nilai pelacak setelah tahap kedua (nilai akhir) = " + str(nilaiAkhir))
print("Status sKrasny = " + status)
print("Status siklus = " + siklus)
