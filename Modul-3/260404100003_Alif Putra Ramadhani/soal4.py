penuh = 0
print()
for i in range(10):
    print("Mahasiswa ke-", i + 1)

    while True:
        print("Contoh Penulisan Nama: Alif")
        nama = input("Nama: ")

        ada_huruf = False   # ada karakter selain spasi?
        ada_angka = False   # ada angka di dalam nama?
        for karakter in nama:
            if karakter != " ":
                ada_huruf = True
            if karakter in "0123456789":
                ada_angka = True

        if not ada_huruf:
            print("Peringatan: nama tidak boleh kosong!")
        elif ada_angka:
            print("Peringatan: nama tidak boleh mengandung angka!")
        else:
            break

    while True:
        teks = input("Masukkan IPK (0.00 - 4.00): ")

        jumlah_titik = 0
        desimal = 0          # banyak angka di belakang titik
        ada_angka = False
        semua_valid = True
        for karakter in teks:
            if karakter == ".":
                jumlah_titik += 1
            elif karakter in "0123456789":
                ada_angka = True
                if jumlah_titik == 1:
                    desimal += 1
            else:
                semua_valid = False

        if teks == "":
            print("Peringatan: IPK tidak boleh kosong!")
        elif teks[0] == "-":
            print("Peringatan: IPK tidak boleh negatif!")
        elif not semua_valid or jumlah_titik > 1 or not ada_angka:
            print("Peringatan: IPK harus berupa angka (desimal pakai titik)!")
        elif desimal > 2:
            print("Peringatan: maksimal 2 angka di belakang titik!")
        elif float(teks) > 4:
            print("Peringatan: IPK harus antara 0.00 dan 4.00!")
        else:
            break

    ipk = float(teks)

    while True:
        print("Contoh Penulisan Penghasilan: 1000000")
        teks = input("Masukkan Penghasilan orang tua: ")

        semua_angka = True
        for karakter in teks:
            if karakter not in "0123456789":
                semua_angka = False

        if teks == "":
            print("Peringatan: penghasilan tidak boleh kosong!")
        elif teks[0] == "-":
            print("Peringatan: penghasilan tidak boleh negatif!")
        elif not semua_angka:
            print("Peringatan: penghasilan harus berupa angka bulat!")
        else:
            break

    gaji = int(teks)

    if ipk < 3.00:
        print(nama, "- tidak memenuhi syarat")
        continue

    if gaji <= 3000000:
        print(nama, "- beasiswa penuh")
        penuh += 1
    elif gaji <= 5000000:
        print(nama, "- beasiswa sebagian")
    else:
        print(nama, "- tidak dapat beasiswa")

    if penuh == 3:
        print("Kuota beasiswa penuh, seleksi dihentikan.")
        break
    print()