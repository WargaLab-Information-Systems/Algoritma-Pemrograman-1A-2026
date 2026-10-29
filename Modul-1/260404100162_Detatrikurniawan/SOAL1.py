kode = int(input())
d1 = int(float(kode) / 100)
d2 = int(float(kode) / 10) % 10
d3 = kode % 10
pelacak = d1 * d3
print("d1 = " + str(d1) + ", d2 = " + str(d2) + ", d3 = " + str(d3) + ", pelacak awal = " + str(pelacak))
if d2 % 2 == 1:
    pelacak = int(float(pelacak) / 3)
else:
    pelacak = pelacak * 2
print("Nilai akhir: " + str(pelacak))
if pelacak % 3 == 0:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - d2
print("Pelacak tahap 1: " + str(pelacak))
if pelacak > 50:
    print("Kategori A")
else:
    if pelacak > 20:
        print("Kategori B")
    else:
        print("sKrasny Ditolak")
if pelacak % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")
