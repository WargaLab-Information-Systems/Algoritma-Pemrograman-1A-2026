penuh = 0

for i in range(10):
    print("Mahasiswa ke-", i + 1)
    nama = input("Nama : ")
    ipk = float(input("IPK : "))
    gaji = int(input("Penghasilan orang tua: Rp"))

    if ipk < 3.00:
        print(nama, "-> tidak memenuhi syarat")
        continue

    if gaji <= 3000000:
        print(nama, "-> beasiswa PENUH")
        penuh = penuh + 1
    elif gaji <= 5000000:
        print(nama, "-> beasiswa SEBAGIAN")
    else:
        print(nama, "-> tidak dapat beasiswa")

    if penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi, seleksi berhenti.")
        break