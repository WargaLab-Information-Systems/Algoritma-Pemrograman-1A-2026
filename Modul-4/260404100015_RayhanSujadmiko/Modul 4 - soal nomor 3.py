print("=== DUA PIRAMIDA ANGKA BERHADAPAN ===")

n = 0
inputan = False

while inputan == False:
    bilangan = input("Masukkan bilangan bulat positif n: ")
    if bilangan == "":
        print("Input tidak boleh kosong, silakan ulangi.") 
    else:
        angka = True
        for karakter in bilangan:
            if karakter not in "0123456789":
                angka = False
                
        if angka == False:
            print("Input harus berupa bilangan bulat positif, silakan ulangi.")
        else:
            n = int(bilangan)
            if n < 1:
                print("Input harus bilangan positif (minimal 1), silakan ulangi.")
            else:
                inputan = True

print()

for i in range(1, n + 1):
    for s in range(n - i):
        print("  ", end="")
    for k in range(1, i + 1):
        print(k, end=" ")

    for g in range(3):
        print(" ", end="")

    for k in range(i, 0, -1):
        print(k, end=" ")
    print()