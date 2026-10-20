penuh = 0

for i in range(10):
    print("\nMahasiswa Ke - ", i + 1)

    # akan diulang jika kosong/hanya angka/angka negatif 
    while True:
        nama = input("\nMasukkan Nama Mahasiswa = ")
        namaAngka = True
        for karakter in nama:
            if (karakter < "0" or karakter > "9") and karakter != "-":
                namaAngka = False
        if nama != "" and namaAngka == False:
            break
        print("Maaf, yang anda inputkan itu salah")

    # akan diulang jika kosong/bukan angka/negatif/lebih dari 4 
    while True:
        ipk = input("Masukkan IPK Mahasiswa = ")
        valid = True
        jumlahTitik = 0
        jumlahAngka = 0
        for karakter in ipk:
            if karakter == ".":
                jumlahTitik += 1
            elif karakter >= "0" and karakter <= "9":
                jumlahAngka += 1
            else:
                valid = False
        if valid == True and jumlahTitik <= 1 and jumlahAngka > 0:
            ipk = float(ipk)
            if ipk <= 4:
                break
        print("Maaf, yang anda inputkan itu salah")

    # diulang jika kosong/bukan angka/negatif 
    while True:
        penghasilan = input("Masukkan Pengahasilan Orang Tua = ")
        valid = penghasilan != ""
        for karakter in penghasilan:
            if karakter < "0" or karakter > "9":
                valid = False
        if valid == True:
            penghasilan = int(penghasilan)
            break
        print("Maaf, yang anda inputkan itu salah")

    if ipk < 3.00:
        print(nama, "~> Maaf Mahasiswa Ini Tidak Memenuhi Syarat")
        continue

    if penghasilan <= 3000000:
        print(nama, "\nSelamat Anda Mendapatkan Beasiswa Penuh")
        penuh += 1
        if penuh == 3:
            print("\nMohon Maaf, Kuota Beasiswa Sudah Penuh, Jangan Menyerah Ya")
            break
    elif penghasilan <= 5000000:
        print(nama, "Selamat Anda Mendapatkan Beasiswa Setengah")
    else:
        print(nama, "Mohon Maaf, Anda Tidak Mendapatkan Beasiswa, Jangan Menyerah")