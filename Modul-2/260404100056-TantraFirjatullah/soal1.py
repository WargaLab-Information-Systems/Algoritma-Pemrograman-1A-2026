kodeUser = int(input("Masukkan kode 3 digit: "))
if len(str(kodeUser)) != 3 or kodeUser < 0:
    print("Kode tidak valid, tidak dapat memproses kode.")
    exit()

digit = [
    kodeUser // 100,            # digit satu
    (kodeUser // 10) % 10,      # digit dua
    kodeUser % 10               # digit tiga
]
nPelacakAwal = digit[0] * digit[2]

if (digit[1] % 2) == 1:
    nPelacakP1 = nPelacakAwal + 25
else:
    nPelacakP1 = nPelacakAwal - digit[1]

if (nPelacakP1 % 3) == 0:
    nPelacakP2 = nPelacakP1 // 3
else:
    nPelacakP2 = nPelacakP1 * 2

if nPelacakP2 > 50:
    status = "Kategori A"
elif nPelacakP2 > 20:
    status = "Kategori B"
else:
    status = "sKrasny tidak valid"

print(f"Digit pertama adalah: {digit[0]}")
print(f"Digit kedua adalah: {digit[1]}")
print(f"Digit ketiga adalah: {digit[2]}")
print(f"Nilai pelacak awal adalah: {nPelacakAwal}")
print(f"Nilai pelacak tahap satu adalah: {nPelacakP1}")
print(f"Nilai pelacak akhir adalah: {nPelacakP2}")
print(f"Status sKrasny adalah: {status}")
