# perulangan while
while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

    if 2 <= n <= 15:
        break

    print("Input tidak valid. Masukkan angka 2 sampai 15.")
# perulangan for
for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
    angka = ""

    for j in range(1, i + 1):
        angka += str(j % 10)

    for j in range(i - 1, 0, -1):
        angka += str(j % 10)

    print(angka.center(2 * n - 1))
