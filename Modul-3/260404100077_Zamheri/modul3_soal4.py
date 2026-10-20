penuh = 0
sebagian = 0
tidak_dapat = 0
tidak_memenuhi = 0

for i in range(1, 11):
    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat beasiswa.")
        tidak_memenuhi += 1
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan: Rp"))

    if penghasilan <= 3000000:
            print(nama, "mendapatkan beasiswa penuh.")
            penuh += 1
            if penuh == 3:
                print("Kuota beasiswa penuh telah terpenuhi.")
                break

    elif penghasilan <= 5000000:
        print(nama, "mendapatkan beasiswa sebagian.")
        sebagian += 1

    else:
        print(nama, "tidak mendapatkan beasiswa.")
        tidak_dapat += 1

print("\n===== REKAP SELEKSI =====")
print("Beasiswa penuh              :", penuh)
print("Beasiswa sebagian           :", sebagian)
print("Tidak mendapat beasiswa     :", tidak_dapat)
print("Tidak memenuhi syarat (IPK) :", tidak_memenuhi)