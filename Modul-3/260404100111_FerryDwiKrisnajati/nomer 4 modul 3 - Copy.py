
jumlah_penuh = 0

for i in range(1, 11):
    if jumlah_penuh == 3:
         print("Kuota beasiswa penuh terpenuhi!")
         break

    print("Mahasiswa ke-", i)
    nama = input("Nama: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat.")
        continue

    penghasilan = int(input("Penghasilan orang tua: "))

    if penghasilan <= 3000000:
        print("Mendapat beasiswa penuh.")
        jumlah_penuh = jumlah_penuh + 1

    elif penghasilan <= 5000000:
        print("Mendapat beasiswa sebagian.")

    else:
        print("Tidak mendapatkan beasiswa.")

print("Jumlah penerima beasiswa penuh:", jumlah_penuh)