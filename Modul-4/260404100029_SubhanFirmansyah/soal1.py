while 1:
    teks = input("Jumlah baris lampu: ")
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

    jumlah_baris = int(teks)                       
    if jumlah_baris < 0:                           
        print("Input tidak boleh negatif, ulangi")
        continue
    if jumlah_baris == 0:
        print("Jumlah baris minimal 1, ulangi")
        continue
    break

while 1:
    teks = input("Jumlah lampu pada setiap baris: ")
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

    jumlah_lampu = int(teks)
    if jumlah_lampu < 0:
        print("Input tidak boleh negatif, ulangi")
        continue
    if jumlah_lampu == 0:
        print("Jumlah lampu minimal 1, ulangi")
        continue
    break

print()

for baris in range(1, jumlah_baris + 1):           
    print("--- Baris", baris, "---")

    for lampu in range(1, jumlah_lampu + 1):       
        if lampu % 3 == 0:                         
            print("Lampu", lampu, "mengalami gangguan")
        else:
            print("Lampu", lampu, "berfungsi normal")

    print()

print("Pemeriksaan sumber listrik utama taman")