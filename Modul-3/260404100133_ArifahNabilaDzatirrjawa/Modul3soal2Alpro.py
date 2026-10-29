while True:
    n = int(input("Masukkan Tinggi Menara: "))

    if n >= 2 and n <= 15:
        break
    else:
        print("Tinggi Menara Harus Antara 2 Sampai 15")

for baris in range(1, n + 1):

    print(" " * (n - baris), end="")

    for angka in range(1, baris + 1):
        print(angka % 10, end="")

    for angka in range(baris - 1, 0, -1):
        print(angka % 10, end="")

    print()

for baris in range(n - 1, 0, -1):

    print(" " * (n - baris), end="")

    for angka in range(1, baris + 1):
        print(angka % 10, end="")

    for angka in range(baris - 1, 0, -1):
        print(angka % 10, end="")

    print()
