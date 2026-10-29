
print("=== PROGRAM MENARA LAMPU HIAS ===")

# Meminta input tinggi yang valid
while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

    if 2 <= n <= 15:
        break
    else:
        print("Tinggi tidak valid! Masukkan angka 2 sampai 15.")

# Membuat bagian atas hingga tengah
for i in range(1, n + 1):
    print(" " * (n - i) * 2, end="")

    for j in range(1, i + 1):
        print(j % 10, end=" ")

    for j in range(i - 1, 0, -1):
        print(j % 10, end=" ")

    print()

# Membuat bagian bawah
for i in range(n - 1, 0, -1):
    print(" " * (n - i) * 2, end="")

    for j in range(1, i + 1):
        print(j % 10, end=" ")

    for j in range(i - 1, 0, -1):
        print(j % 10, end=" ")

    print()
