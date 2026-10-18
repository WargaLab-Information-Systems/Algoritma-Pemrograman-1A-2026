penuh = 0
sebagian = 0
tidak_dapat = 0
tidak_memenuhi = 0
diproses = 0

for i in range(1, 11):
    print("=== Mahasiswa ke-", i, "===")

    while 1:
        nama = input("Nama                  : ")
        if nama == "":
            print("Nama tidak boleh kosong, ulangi")
            continue

        ada_angka = False
        ada_huruf = False
        for huruf in nama:
            if huruf >= "0" and huruf <= "9":
                ada_angka = True
            if huruf != " ":
                ada_huruf = True

        if ada_huruf == False:
            print("Nama tidak boleh kosong, ulangi")
            continue
        if ada_angka:
            print("Nama tidak boleh mengandung angka, ulangi")
            continue
        break

    while 1:
        teks = input("IPK (pakai titik)     : ")
        if teks == "":
            print("IPK tidak boleh kosong, ulangi")
            continue

        angka_valid = True
        jumlah_angka = 0
        jumlah_titik = 0
        posisi = 0
        for huruf in teks:
            posisi += 1
            if posisi == 1 and huruf == "-":
                pass
            elif huruf == ".":
                jumlah_titik += 1
            elif huruf >= "0" and huruf <= "9":
                jumlah_angka += 1
            else:
                angka_valid = False

        if angka_valid == False or jumlah_angka == 0 or jumlah_titik > 1:
            print("IPK harus berupa angka (contoh 3.50), ulangi")
            continue

        ipk = float(teks)
        if ipk < 0:
            print("IPK tidak boleh negatif, ulangi")
            continue
        if ipk > 4:
            print("IPK tidak boleh lebih dari 4.00, ulangi")
            continue
        break

    while 1:
        teks = input("Penghasilan orang tua : ")
        if teks == "":
            print("Penghasilan tidak boleh kosong, ulangi")
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
            print("Penghasilan harus berupa bilangan bulat tanpa titik, ulangi")
            continue

        penghasilan = int(teks)
        if penghasilan < 0:
            print("Penghasilan tidak boleh negatif, ulangi")
            continue
        break

    diproses += 1

    if ipk < 3.00:                                 
        print(nama, ": tidak memenuhi syarat (IPK < 3,00)")
        print()
        tidak_memenuhi += 1
        continue

    if penghasilan <= 3000000:
        print(nama, ": beasiswa PENUH")
        penuh += 1
    elif penghasilan <= 5000000:
        print(nama, ": beasiswa SEBAGIAN")
        sebagian += 1
    else:
        print(nama, ": tidak mendapat beasiswa (penghasilan > Rp5.000.000)")
        tidak_dapat += 1
    print()

    if penuh == 3:                                 
        print("Kuota beasiswa penuh (3 mahasiswa) terpenuhi, seleksi dihentikan")
        print()
        break

print("===== REKAP SELEKSI =====")
print("Mahasiswa diproses          :", diproses)
print("Beasiswa penuh              :", penuh)
print("Beasiswa sebagian           :", sebagian)
print("Tidak mendapat beasiswa     :", tidak_dapat)
print("Tidak memenuhi syarat (IPK) :", tidak_memenuhi)