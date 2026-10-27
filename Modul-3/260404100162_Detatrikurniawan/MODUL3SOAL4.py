penuh = 0
sebagian = 0
tidak = 0
tidak_memenuhi = 0

for i in range(1, 3):
    print(f"\nMahasiswa ke {i}")
    nama = input("Nama                   : ")
    ipk = float(input("IPK                    : "))
    penghasilan = float(input("Penghasilan orang tua : "))

    if ipk < 3.00:
        print(f"{nama}: IPK tidak memenuhi syarat, dilewati.")
        tidak_memenuhi += 1
        continue
    if penghasilan <= 3000000:
        print(f"{nama}: Mendapatkan BEASISWA PENUH")
        penuh += 1
    elif penghasilan <= 5000000:
        print(f"{nama}: Mendapatkan BEASISWA SEBAGIAN")
        sebagian += 1
    else:
        print(f"{nama}: Tidak mendapatkan beasiswa")
        tidak += 1

    if penuh == 3:
        print("\nKuota beasiswa penuh (3 mahasiswa) sudah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break
print("\nREKAP")
print("Beasiswa penuh         :", penuh)
print("Beasiswa sebagian      :", sebagian)
print("Tidak dapat beasiswa   :", tidak)
print("IPK tidak memenuhi     :", tidak_memenuhi)