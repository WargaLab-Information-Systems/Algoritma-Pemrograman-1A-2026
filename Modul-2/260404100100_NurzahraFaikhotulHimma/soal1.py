print("SISTEM BRANKAS sKrasny")
print("Masukkan kode 3 digit")
kode = int(input())
digit1 = float(kode) / 100
print("digitnya pertama " + str(digit1))
digit2 = float(kode) / 10 % 10
print("digitnya kedua " + str(digit2))
digit3 = kode % 10
print("digitnya ketiga " + str(digit3))
pelacakAwal = digit1 * digit3
print("Pelacak awal yaitu " + str(pelacakAwal))
if digit2 % 2 == 1:
    pelacakTahap1 = pelacakAwal + 25
else:
    pelacakTahap1 = pelacakAwal + digit2
print("Pelacak tahap1 yaitu " + str(pelacakTahap1))
if pelacakTahap1 % 3 == 0:
    pelacakAkhir = float(pelacakTahap1) / 3
else:
    pelacakAkhir = pelacakTahap1 * 2
print("Nilai akhir yaitu " + str(pelacakAkhir))
if pelacakAkhir > 50:
    print("Status sKrasny: Kategori A")
else:
    if pelacakAkhir > 20:
        print("Status sKrasny Kategori B")
    else:
        print("Status sKrasny Ditolak")
if pelacakAkhir % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")
