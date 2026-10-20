# Soal 2 - Menara Lampu Hias

# validasi input
while True:
    teks = input("Masukkan tinggi setengah menara (2-15): ")

    semua_angka = True
    for karakter in teks:
        if karakter not in "0123456789":
            semua_angka = False

    if teks == "":
        print("Peringatan: input tidak boleh kosong!")
    elif teks[0] == "-":
        print("Peringatan: input tidak boleh negatif!")
    elif not semua_angka:
        print("Peringatan: input harus berupa angka bulat!")
    elif int(teks) < 2 or int(teks) > 15:
        print("Peringatan: harus antara 2 sampai 15!")
    else:
        break

n = int(teks)

# Menara atas
for i in range(1, n + 1):
    baris = ""
    for angka in range(1, i + 1):
        baris += str(angka % 10)
    for angka in range(i - 1, 0, -1):
        baris += str(angka % 10)
    print(" " * (n - i) + baris)

# Menara bawah
for i in range(n - 1, 0, -1):
    baris = ""
    for angka in range(1, i + 1):
        baris += str(angka % 10)
    for angka in range(i - 1, 0, -1):
        baris += str(angka % 10)
    print(" " * (n - i) + baris)