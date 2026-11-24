n = int(input("Masukkan tinggi piramida: "))

while n <= 0:
    print("Tinggi harus lebih dari 0!")
    n = int(input("Masukkan tinggi piramida: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end="")

    for spasi in range(1, (n - i) * 2 + 3):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()