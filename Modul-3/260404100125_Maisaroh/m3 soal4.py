jumlahBeasiswaPenuh = 0

for i in range(1, 11):
    print("mahasiswa ke-", i)

    nama = input("masukkan nama mahasiswa: ")
    ipk = float(input("masukkan IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat beasiswa")
        continue

    penghasilan = float(input("masukkan penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        if jumlahBeasiswaPenuh < 3:
            status = "beasiswa penuh"
            jumlahBeasiswaPenuh += 1
        else:
            status = "tidak mendapatkan beasiswa"
    elif penghasilan <= 5000000:
        status = "beasiswa sebagian"
    else:
        status = "tidak mendapatkan beasiswa"

    print("nama:", nama)
    print("IPK:", ipk)
    print("status:", status)

    if jumlahBeasiswaPenuh == 3:
        print("kuota beasiswa penuh sudah terpenuhi")
        break

print("jumlah penerima beasiswa penuh:", jumlahBeasiswaPenuh)
