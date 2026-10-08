print("masukkan kode rahasia 3 digit")
d1 = int(input())
print("nilal digit1=" + str(d1))
d2 = int(input())
print("nilai digit2=" + str(d2))
d3 = int(input())
print("nilai digit3=" + str(d3))
nilaiAwal = d1 * d3
print("nilai pelacak awal=" + str(nilaiAwal))
if d2 % 2 == 0:
    nilaiTahap1 = nilaiAwal + 25
else:
    nilaiTahap1 = nilaiAwal - d2
print("nilai tahap 1=" + str(nilaiTahap1))
if nilaiTahap1 % 3 == 0:
    nilaiAkhir = float(nilaiTahap1) / 3
else:
    nilaiAkhir = nilaiTahap1 * 2
print("nilai akhir=" + str(nilaiAkhir))
if nilaiAkhir > 50:
    status = "A"
else:
    if nilaiAkhir > 20:
        status = "B"
    else:
        status = "sKrasnyDitolak"
print("status=" + status)
if nilaiAkhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"
print("siklus=" + siklus)
