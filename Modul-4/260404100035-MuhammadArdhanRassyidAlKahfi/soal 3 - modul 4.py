while True:
    teks = input("Masukkan bilangan bulat positif (1-9) n: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isdigit():
        print("Input harus berupa bilangan bulat positif!")
    elif int(teks) <= 0:
        print("Bilangan harus lebih dari 0!")
    else:
        n = int(teks)
        break

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    for spasi in range(1, 2 * (n - i) + 2):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()