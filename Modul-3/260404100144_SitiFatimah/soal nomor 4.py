
jumlah_penuh = 0

for i in range(1, 11):

    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break

    print("Mahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat beasiswa.")
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        if jumlah_penuh < 3:
            status = "Beasiswa penuh"
            jumlah_penuh += 1
        else:
            status = "Kuota beasiswa penuh habis"

    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"

    else:
        status = "Tidak mendapatkan beasiswa"

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Status:", status)

print("Jumlah penerima beasiswa penuh:", jumlah_penuh)
