digit = [0] * (3)

print("Masukkan kode 3 digit: ", end='', flush=True)
kodeUser = int(input())
digit[0] = float(kodeUser) / 100
digit[1] = float(kodeUser) / 10 % 10
digit[2] = kodeUser % 10
nPelacakAwal = digit[0] * digit[2]
if digit[1] % 2 == 1:
    nPelacakP1 = nPelacakAwal + 25
else:
    nPelacakP1 = nPelacakAwal - digit[1]
if nPelacakP1 % 3 == 0:
    nPelacakP2 = float(nPelacakP1) / 3
else:
    nPelacakP2 = nPelacakP1 * 2
if nPelacakP2 > 50:
    status = "Kategori A"
else:
    if nPelacakP2 > 20:
        status = "Kategori B"
    else:
        status = "sKrasny tidak valid"
print("Digit pertama adalah: " + str(digit[0]))
print("Digit kedua adalah: " + str(digit[1]))
print("Digit ketiga adalah: " + str(digit[2]))
print("Nilai pelacak awal adalah: " + str(nPelacakAwal))
print("Nilai pelacak tahap satu adalah: " + str(nPelacakP1))
print("Nilai pelacak akhir adalah: " + str(nPelacakP2))
print("Status sKrasny adalah: " + status)
if nPelacakP2 % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")
