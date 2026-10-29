print("masukkan kode 3 digit")
kode = int(input())
digit1 = float(kode) / 100
digit2 = float(kode) / 10 % 10
digit3 = kode % 10
print("digit pertama = " + str(digit1))
print("digit kedua= " + str(digit2))
print("digit ketiga= " + str(digit3))
pelacak = digit1 * digit3
print("nilai pelacak awal= " + str(pelacak))
if digit2 % 2 == 1:
    pelacak = pelacak + 25
else:
    pelacak = pelacak + digit2
print("nilai akhir = " + str(pelacak))
if pelacak > 50:
    print("kategori a")
else:
    if pelacak > 20:
        print("kategori b")
    else:
        print("skrasnya ditolak")
    if pelacak < 20:
        print("siklus genap")
    else:
        print("siklus ganjil")
