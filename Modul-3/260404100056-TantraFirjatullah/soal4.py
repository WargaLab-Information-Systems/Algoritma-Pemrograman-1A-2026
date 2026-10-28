mahasiswa= []
banyak = 10
counter = 0

for i in range(banyak):
    print()
    while True:
        nama = input(f"Masukkan nama mahasiswa {i + 1}: ")
        if nama != "":
            break
        else:
            print("Nama tidak boleh kosong!")

    while True:
        try:
            ipk = float(input("Nilai IPK: "))
        except ValueError:
            print("Harus berupa angka!")
            continue
        if ipk < 0 or ipk > 4:
            print("Nilai harus antara 0 dan 4!")
            continue
        break

    while True:
        try:
            penghasilan = int(input("Penghasilan Orang Tua: Rp"))
        except ValueError:
            print("Harus berupa angka!")
            continue
        if penghasilan < 0:
            print("Nilai harus positif!")
            continue
        break

    if ipk >= 3:
        status = "Dapat Beasiswa Penuh" if penghasilan <= 3000000 else "Dapat Beasiswa Sebagian" if penghasilan <= 5000000 else "Tidak Dapat Beasiswa"
        counter += 1 if penghasilan <= 3000000 else 0
    else:
        print(f"Mahasiswa {i+1} tidak layak.")
        continue

    data = {
        "nama": nama,
        "ipk": ipk,
        "penghasilan": penghasilan,
        "status": status
    }

    mahasiswa.append(data)
    if counter >= 3:
        break

print()

for m in mahasiswa:
    print(f"{m["nama"]}, {m["status"]}")
