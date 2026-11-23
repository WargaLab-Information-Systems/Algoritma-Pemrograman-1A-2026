print("SISTEM BRANKAS sKrasny")
print("Masukkan kode 3 digit: ", end='', flush=True)
kode = int(input())
digit1 = float(kode) / 100
digit2 = float(kode) / 10 % 10
digit3 = kode % 10
print("Digit pertama: " + str(digit1))
print("Digit kedua: " + str(digit2))
print("Digit ketiga: " + str(digit3))
pelacakAwal = digit1 * digit3
print("Pelacak awal: " + str(pelacakAwal))
if digit2 % 2 == 1:
    pelacakTahap1 = pelacakAwal + 25
else:
    pelacakTahap1 = pelacakAwal - digit2
print("Pelacak tahap 1: " + str(pelacakTahap1))
if pelacakTahap1 % 3 == 0:
    nilaiAkhir = float(pelacakTahap1) / 3
else:
    nilaiAkhir = pelacakTahap1 * 2
print("Nilai akhir: " + str(nilaiAkhir))
if nilaiAkhir > 50:
    print("Status sKrasny: Kategori A")
else:
    if nilaiAkhir > 20:
        print("Status sKrasny: Kategori B")
    else:
        print("Status sKrasny: sKrasny Ditolak")
if nilaiAkhir % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")
