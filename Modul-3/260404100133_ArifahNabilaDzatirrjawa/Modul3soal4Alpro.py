
jumlah_penuh = 0
jumlah_sebagian = 0
jumlah_tidak_dapat = 0
jumlah_ipk_tidak_lolos = 0

for i in range(1, 11):
    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break

    print("Mahasiswa ke-", i)
    nama = str(input("Masukkan nama mahasiswa: "))
    ipk = float(input("Masukkan IPK mahasiswa: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat IPK.")
        jumlah_ipk_tidak_lolos = jumlah_ipk_tidak_lolos + 1
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan (Rp): "))

    if penghasilan <= 3000000:
        status = "Beasiswa penuh"
        jumlah_penuh = jumlah_penuh + 1
    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"
        jumlah_sebagian = jumlah_sebagian + 1
    else:
        status = "Tidak mendapat beasiswa"
        jumlah_tidak_dapat = jumlah_tidak_dapat + 1

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Hasil seleksi:", status)

print("HASIL SELEKSI BEASISWA")
print("Beasiswa penuh:", jumlah_penuh, "mahasiswa")
print("Beasiswa sebagian:", jumlah_sebagian, "mahasiswa")
print("Tidak mendapat beasiswa:", jumlah_tidak_dapat, "mahasiswa")
print("Tidak lolos syarat IPK:", jumlah_ipk_tidak_lolos, "mahasiswa")
