while True:
    n = input("Masukkan Angka Max nya = ")
    huruf = n != ""
    for karakter in n:
        if karakter < "0" or karakter > "9":
            huruf = False
    if huruf == True:
        n = int(n)
        break
    print("Dilarang memasukkan input Angka Minus(-), Input Yang selain di suruh, (Contoh Yang Benar -----> 3)")

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(k, end=" ")

    print("|", end=" ")

    for k in range(i, 0, -1):
        print(k, end=" ")
    print()