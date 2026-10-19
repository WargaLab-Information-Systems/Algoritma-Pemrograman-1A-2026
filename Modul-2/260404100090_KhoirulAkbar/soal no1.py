print("masukkan kode rahasia 3 digit angka")
digit1 = int(input())
print("digit1 = " + str(digit1))
digit2 = int(input())
print("digit2 = " + str(digit2))
digit3 = int(input())
print("digit3 = " + str(digit3))
pelacakAwal = digit1 * digit3
pelacakTahap1 = pelacakAwal
if digit2 % 2 != 0:
    pelacakTahap1 = pelacakTahap1 + 25
else:
    pelacakTahap1 = pelacakTahap1 - digit2
if pelacakTahap1 % 3 == 0:
    nilaiAkhir = float(pelacakTahap1) / 3
else:
    nilaiAkhir = pelacakTahap1 * 2
if nilaiAkhir > 50:
    status = "Kategori A"
else:
    if nilaiAkhir > 20:
        status = "Kategori B"
    else:
        status = "sKrasny Ditolak"
print(" Nilai pelacak awal = " + str(pelacakAwal))
print(" Nilai pelacak tahap pertama = " + str(pelacakTahap1))
print(" Nilai akhir = " + str(nilaiAkhir))
print(" Status sKrasny = " + status)
if nilaiAkhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"
print(" siklus = " + siklus)
