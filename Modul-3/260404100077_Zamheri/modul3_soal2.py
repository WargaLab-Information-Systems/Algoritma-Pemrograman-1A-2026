
while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

    if n >= 2 and n <= 15:
        break
    else:
        print("Tinggi harus antara 2 sampai 15!")

for i in range(1, n + 1):
    for spasi in range(n - i):
        print(" ", end="")

    for angka in range(1, i + 1):
        print(angka % 10, end="")

    for angka in range(i - 1, 0, -1):
        print(angka % 10, end="")

    print()


for i in range(n - 1, 0, -1):
    for spasi in range(n - i):
        print(" ", end="")

    for angka in range(1, i + 1):
        print(angka % 10, end="")

    for angka in range(i - 1, 0, -1):
        print(angka % 10, end="")

    print()
