kuota_penuh = 0

for i in range(10):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("Nama:", nama)
        print("Hasil: Tidak memenuhi syarat")
        continue

    penghasilan = float(input("Masukkan penghasilan orang tua: "))

    if penghasilan <= 3000000:
        print("Nama:", nama)
        print("Hasil: Beasiswa penuh")
        kuota_penuh += 1

    elif penghasilan <= 5000000:
        print("Nama:", nama)
        print("Hasil: Beasiswa sebagian")

    else:
        print("Nama:", nama)
        print("Hasil: Tidak mendapatkan beasiswa")

    if kuota_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        break

print("\nProses seleksi selesai.")
print("Jumlah penerima beasiswa penuh:", kuota_penuh)