#  PEMISAHAN DIGIT
kode = int(input("Masukkan kode rahasia 3 digit : "))

digit1 = kode // 100
digit2 = (kode // 10) % 10
digit3 = kode % 10

print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)


# # NILAI PELACAK AWAL
pelacak = digit1 * digit3

print("Nilai pelacak awal :", pelacak)


# # PERUBAHAN TAHAP PERTAMA
if digit2 % 2 == 1 :
    pelacak = pelacak + 25
else :
    pelacak = pelacak - digit2

print("Nilai pelacak setelah tahap pertama :", pelacak)


# # PERUBAHAN TAHAP KEDUA
if pelacak % 3 == 0 :
    pelacak = pelacak // 3
else :
    pelacak = pelacak * 2

print("Nilai pelacak setelah tahap kedua :", pelacak)


# # STATUS SKRASNY
if pelacak > 50 :
    print("Status sKrasny : Kategori A")
elif pelacak > 20 :
    print("Status sKrasny : Kategori B")
else :
    print("Status sKrasny : sKrasny Ditolak")


# # SIKLUS
if pelacak % 2 == 0 :
    print("Siklus Genap")
else :
    print("Siklus Ganjil")