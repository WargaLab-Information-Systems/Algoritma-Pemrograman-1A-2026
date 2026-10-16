# Input tinggi setengah menara
while True:
    try:
        input_n = input("Masukkan tinggi setengah menara (2-15): ")

        # Mengecek input kosong
        if input_n.strip() == "":
            print("Input tidak boleh kosong!")
            continue

        n = int(input_n)

        # Mengecek angka di luar rentang
        if n < 2 or n > 15:
            print("Input tidak valid! Masukkan angka 2 sampai 15.")
            continue

        break

    except ValueError:
        print("Tolong masukkan angka, bukan teks atau kalimat.")

while n < 2 or n > 15:
    print("Input tidak valid!")
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()