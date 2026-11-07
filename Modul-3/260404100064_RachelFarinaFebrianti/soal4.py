penuh = 0

for i in range(1, 11):
    if penuh >= 3:
        break
    print("Mahasiswa ke-", i)
    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))
    if ipk < 3.00:
        print(nama, ": Tidak memenuhi syarat (IPK < 3.00), dilewati")
        continue
    penghasilan = int(input("Masukkan penghasilan orang tua: Rp"))
    if penghasilan <= 3000000:
        status = "Beasiswa Penuh"
        penuh = penuh + 1
    elif penghasilan <= 5000000:
        status = "Beasiswa Sebagian"
    else:
        status = "Tidak Mendapat Beasiswa"
    print("Hasil seleksi", nama, ":", status)
    if penuh >= 3:
        print("Kuota beasiswa penuh tercapai, seleksi dihentikan.")
        break

print("Jumlah penerima beasiswa penuh :", penuh)
