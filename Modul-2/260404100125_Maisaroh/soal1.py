kode = int(input("masukkan kode 3 digit: "))

# memisahkan 3 digit
digit1 = kode//100
digit2 = (kode//10) % 10
digit3 = kode % 10 
print("digit pertama :", digit1)
print("digit kedua :", digit2)
print("digit ketiga :", digit3)

# nilai pelacak awal
pelacak = digit1 * digit3
print("nilai pelacak awal :", pelacak)

# perubahan tahap pertama
if digit2 % 2 == 1:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - digit2
print("pelacak tahap pertama :", pelacak)

# perubahan tahap kedua
if pelacak % 3 == 0:
    pelacak = pelacak // 3
else:
    pelacak = pelacak * 2
print("nilai akhir :", pelacak)

# menetukan kategori
if pelacak > 50:
    print("status : kategori A")
elif pelacak > 20:
    print("status : kategori B")
else:
    print("status : sKrasny ditolak")

# menentukan siklus
if pelacak % 2 == 0:
    print("siklus genap")
else:
    print("siklus ganjil")