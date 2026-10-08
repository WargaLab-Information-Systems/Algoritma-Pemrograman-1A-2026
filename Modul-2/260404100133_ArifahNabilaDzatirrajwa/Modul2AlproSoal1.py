kodeRahasia = int(input("Masukkan kode rahasia 3 digit: "))

digit1 = kodeRahasia // 100
digit2 = (kodeRahasia // 10) % 10
digit3 = kodeRahasia % 10

print("Digit pertama: ", digit1)
print("Digit kedua: ", digit2)
print("Digit ketiga: ", digit3)

nilaiPelacak = digit1 * digit3
print("Nilai Pelacak Awal: ", nilaiPelacak)

if digit2 % 2 == 0:
    nilaiPelacak = nilaiPelacak + 25
else:
    nilaiPelacak = nilaiPelacak - digit2

print("Nilai Pelacak Tahap 1 :", nilaiPelacak)

if nilaiPelacak % 3 == 0:
    nilaiPelacak = nilaiPelacak // 3
else:
    nilaiPelacak = nilaiPelacak * 2

print("Nilai Akhir Pelacak:", nilaiPelacak)

if nilaiPelacak > 50:
    status = "Kategori A"
elif nilaiPelacak > 20:
    status = "Kategori B"
else:
    status = "sKrasny Ditolak"

print("Status sKrasny :", status)

if nilaiPelacak % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")