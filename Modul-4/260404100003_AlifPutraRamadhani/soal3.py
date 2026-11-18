# Program piramida yang saling berhadapan
while True:
    n_str = input("Masukkan Angka: ")
    if not n_str:
        print("Masukan Tidak Boleh Kosong")
        continue
    if n_str[0] == "-":
        print("Masukan Tidak Boleh Minus")
        continue
    n_int = True    
    for karakter in n_str:
        if karakter < '0' or karakter > '9':
            n_int = False
            break
    if not n_int:
        print("Masukan Tidak Boleh Huruf / Karakter")
        continue
    n = int(n_str)
    if n <= 0:
        print("Masukan Harus Bilangan Bulat Positif dan tidak boleh 0")
        continue
    else:
        break

for one in range(1, n + 1):
    for two in range(1, one + 1):
        print(two, end=' ')
    for tre in range(4 * (n - one) + 9):
        print(' ', end='')
    for two in range(one, 0, -1):
        print(two, end=' ')
    print()