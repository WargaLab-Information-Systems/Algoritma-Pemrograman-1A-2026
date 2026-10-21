
jumlah_beasiswa_penuh = 0

for i in range(1, 11):
    if jumlah_beasiswa_penuh == 3:
        print("Kuota beasiswa penuh telah terpenuhi.")
        break

    print("\nMahasiswa ke-", i)

    # Validasi nama mahasiswa
    while True:
        nama = input("Masukkan nama mahasiswa: ").strip()

        if nama == "":
            print("Peringatan: Nama mahasiswa tidak boleh kosong.")
        elif nama.replace(" ", "").isdigit():
            print("Peringatan: Nama harus berupa teks, bukan angka.")
        else:
            break

    # Validasi IPK
    while True:
        input_ipk = input("Masukkan IPK: ").strip()

        if input_ipk == "":
            print("Peringatan: IPK tidak boleh kosong.")
            continue

        try:
            ipk = float(input_ipk)
        except ValueError:
            print("Peringatan: IPK harus berupa angka, bukan teks atau kalimat.")
            continue

        if ipk < 0 or ipk > 4:
            print("Peringatan: IPK harus berada antara 0 dan 4.")
            continue

        break

    if ipk < 3.00:
        print("Tidak memenuhi syarat beasiswa.")
        continue

    # Validasi penghasilan orang tua
    while True:
        input_penghasilan = input(
            "Masukkan penghasilan orang tua per bulan: Rp"
        ).strip()

        if input_penghasilan == "":
            print("Peringatan: Penghasilan tidak boleh kosong.")
            continue

        try:
            penghasilan = int(input_penghasilan)
        except ValueError:
            print("Peringatan: Penghasilan harus berupa angka bulat, bukan teks.")
            continue

        if penghasilan < 0:
            print("Peringatan: Penghasilan tidak boleh negatif.")
            continue

        break

    if penghasilan <= 3000000:
        status = "Beasiswa penuh"
        jumlah_beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"
    else:
        status = "Tidak mendapatkan beasiswa"

    print("Nama:", nama)
    print("Status:", status)

if jumlah_beasiswa_penuh == 3:
    print("Seleksi dihentikan karena kuota beasiswa penuh sudah terpenuhi.")

print("Jumlah penerima beasiswa penuh:", jumlah_beasiswa_penuh)
