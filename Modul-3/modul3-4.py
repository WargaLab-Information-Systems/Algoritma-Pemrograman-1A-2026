penuh = 0      # jumlah penerima beasiswa penuh
sebagian = 0   # jumlah penerima beasiswa sebagian
diproses = 0   # jumlah mahasiswa yang sudah diproses

for i in range(10):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    penghasilan = int(input("Penghasilan orang tua per bulan (Rp): "))
    diproses += 1

    # Lewati mahasiswa yang IPK-nya kurang dari 3.00
    if ipk < 3.00:
        print(f"{nama}: Tidak memenuhi syarat (IPK < 3,00)")
        continue

    # Periksa penghasilan orang tua
    if penghasilan <= 3000000:
        hasil = "Beasiswa Penuh"
        penuh += 1
    elif penghasilan <= 5000000:
        hasil = "Beasiswa Sebagian"
        sebagian += 1
    else:
        hasil = "Tidak mendapat beasiswa"

    print(f"{nama}: {hasil}")

    # Hentikan proses jika kuota beasiswa penuh sudah terpenuhi
    if penuh == 3:
        print("\nKuota beasiswa penuh (3 mahasiswa) sudah terpenuhi, seleksi dihentikan.")
        break

# Rekap
print("\n--- Rekap Seleksi ---")
print("Mahasiswa diproses:", diproses)
print("Beasiswa penuh   :", penuh)
print("Beasiswa sebagian:", sebagian)