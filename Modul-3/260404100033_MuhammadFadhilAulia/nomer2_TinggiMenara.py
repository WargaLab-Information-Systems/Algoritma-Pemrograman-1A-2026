while True:
    n = input("Masukkan Tinggi Setengah Menara(2 - 15) = ")
    valid = n != ""
    for karakter in n:
        if karakter < "0" or karakter > "9":
            valid = False
    if valid == True:
        n = int(n)
        if 2 <= n <= 15:
            break
    print("Tinggi Tidak Valid, Mohon Ulangi")

# Menara atas
for i in range(1, n + 1):
    baris = ""
    for angka in range(1, i + 1):
        baris += str(angka % 10)
    for angka in range(i - 1, 0, -1):
        baris += str(angka % 10)
    print(" " * (n - i) + baris)

# Menara bawah
for i in range(n - 1, 0, -1):
    baris = ""
    for angka in range(1, i + 1):
        baris += str(angka % 10)
    for angka in range(i - 1, 0, -1):
        baris += str(angka % 10)
    print(" " * (n - i) + baris)