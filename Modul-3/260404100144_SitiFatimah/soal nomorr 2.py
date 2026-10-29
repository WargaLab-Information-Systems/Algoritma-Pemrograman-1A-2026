
while True:
    n = int(input("Masukkan tinggi (2-15): "))

    if 2 <= n <= 15:
        break

    print("Input harus antara 2 sampai 15!")

# Bagian atas
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    angka = 1
    while angka <= i:
        print(angka % 10, end="")
        angka += 1

    angka = i - 1
    while angka >= 1:
        print(angka % 10, end="")
        angka -= 1

    print()

# Bagian bawah
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    angka = 1
    while angka <= i:
        print(angka % 10, end="")
        angka += 1

    angka = i - 1
    while angka >= 1:
        print(angka % 10, end="")
        angka -= 1

    print()
