penuh = 0
sebagian = 0

def valid_float(prompt):
    while True:
        x = input(prompt)
        if x.strip() == "":
            print("Input tidak boleh kosong!")
            continue
        if x.count(".") > 1:
            print("Format angka desimal salah!")
            continue
        if not x.replace(".", "", 1).isdigit():
            print("Hanya boleh angka!")
            continue
        return float(x)

for i in range(10):
    print("Mahasiswa ke-", i + 1)
    nama = input("Nama: ")
    while nama.strip() == "":
        print("Nama tidak boleh kosong, ulangi!")
        nama = input("Nama: ")

    ipk = valid_float("IPK: ")
    while True:
        px = input("Penghasilan orang tua: ")
        if px.strip() == "":
            print("Input tidak boleh kosong!")
            continue
        if not px.lstrip("-").isdigit():
            print("Hanya boleh angka!")
            continue
        penghasilan = int(px)
        if penghasilan < 0:
            print("Tidak boleh negatif!")
            continue
        break

    if ipk < 3.00:
        print(nama, "- tidak memenuhi syarat")
        continue

    if penghasilan <= 3000000:
        print(nama, "- beasiswa penuh")
        penuh += 1
    elif penghasilan <= 5000000:
        print(nama, "- beasiswa sebagian")
        sebagian += 1
    else:
        print(nama, "- tidak mendapat beasiswa")

    if penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi, seleksi dihentikan")
        break