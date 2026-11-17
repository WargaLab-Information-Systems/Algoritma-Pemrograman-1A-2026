kode = int(input("Masukkan kode 3 digit: "))

digit1 = kode // 100
digit2 = (kode // 10) % 10
digit3 = kode % 10

print("Digit pertama :", digit1)
print("Digit kedua :", digit2)
print("Digit ketiga :", digit3)

nilai = digit1 * digit3
print("Nilai pelacak awal :", nilai)

if digit2 % 2 == 1: 
    nilai = nilai + 25
else:
 nilai = nilai - digit2
print("Setelah perubahan tahap pertama :", nilai)

if nilai % 3 == 0: 
    nilai = nilai // 3
else:
 nilai = nilai * 2
print("Nilai akhir :", nilai)  
if nilai > 50:
    print("Password terdeteksi sebagai Kategori A") 
elif nilai > 20:
    print("Password terdeteksi sebagai Kategori B") 
else:
    print("Password Ditolak")

if nilai % 2 == 0:
     print("Siklus Genap")
else:
    print("Siklus Ganjil")