jumlah_penuh = 0

for i in range(1, 11):
    if jumlah_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi!")
        break

    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat beasiswa.")
        continue

    penghasilan = int(input("Masukkan penghasilan orang tua: Rp"))

    if penghasilan <= 3000000:
        print("Hasil seleksi: Beasiswa penuh")
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        print("Hasil seleksi: Beasiswa sebagian")
    else:
        print("Hasil seleksi: Tidak mendapatkan beasiswa")

print("\n===== HASIL AKHIR SELEKSI =====")
print("Jumlah penerima beasiswa penuh:", jumlah_penuh)
