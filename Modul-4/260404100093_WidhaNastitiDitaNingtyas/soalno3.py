n = int(input("Masukkan bilangan bulat positif: "))

while n <= 0:
    print("Input harus bilangan positif!")
    n = int(input("Masukkan bilangan bulat positif: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    for k in range(1, 2 * (n - i) + 3):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()