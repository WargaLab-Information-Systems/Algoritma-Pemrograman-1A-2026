while True:
    n = input("Masukkan bilangan bulat positif: ")
    if n == "":
        print("Input tidak boleh kosong!")
    elif n.startswith("-"):
        print("Angka tidak boleh negatif!")
    elif not n.isdigit():
        print("Input harus berupa angka!")
    elif int(n) <= 0:
        print("Angka harus lebih besar dari 0!")
    elif int(n) > 9:
        print("Angka harus lebih kecil dari 10!")
    else:
        n = int(n)
        break

print()

for i in range(1, n + 1):          

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(2 * (n - i) + 2):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")
    print()                        