
print("=== POLA DUA PIRAMIDA ANGKA ===")

# Meminta input bilangan positif
n = int(input("Masukkan bilangan bulat positif: "))

while n <= 0:
    print("Bilangan harus lebih dari 0.")
    n = int(input("Masukkan bilangan bulat positif: "))

for i in range(1, n + 1):

    , i + 1):for j in range(1
        print(j, end="")

    for k in range(1, (2 * (n - i)) + 2):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()
