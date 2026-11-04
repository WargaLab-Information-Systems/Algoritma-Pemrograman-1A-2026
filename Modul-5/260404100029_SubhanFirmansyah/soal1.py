def fibonacci(n):
    if n == 1 or n == 2:                           
        return 1
    else:                                          
        return fibonacci(n - 1) + fibonacci(n - 2)

def baca_hari():
    while 1:
        teks = input("Masukkan hari ke-N: ")
        if teks == "":
            print("Input tidak boleh kosong, ulangi")
            continue

        angka_valid = True
        jumlah_angka = 0
        posisi = 0
        for huruf in teks:
            posisi += 1
            if posisi == 1 and huruf == "-":
                pass
            elif huruf >= "0" and huruf <= "9":
                jumlah_angka += 1
            else:
                angka_valid = False

        if angka_valid == False or jumlah_angka == 0:
            print("Input harus berupa bilangan bulat, ulangi")
            continue

        n = int(teks)
        if n < 0:
            print("Input tidak boleh negatif, ulangi")
            continue
        if n == 0:
            print("N harus bilangan bulat positif (minimal 1), ulangi")
            continue
        return n

hari = baca_hari()

print()
print("Jumlah pelanggan setiap hari:")
for h in range(1, hari + 1):
    print("Hari ke-", h, ":", fibonacci(h), "orang")

pelanggan = fibonacci(hari)

print()
print("Jumlah pelanggan pada hari ke-", hari, ":", pelanggan, "orang")