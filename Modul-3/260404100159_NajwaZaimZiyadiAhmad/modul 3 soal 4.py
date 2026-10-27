
print("=== PROGRAM SELEKSI BEASISWA ===")

jumlah_beasiswa_penuh = 0
jumlah_beasiswa_sebagian = 0
jumlah_tidak_dapat = 0
jumlah_tidak_memenuhi = 0

for i in range(1, 11):
    # Berhenti jika kuota beasiswa penuh sudah terpenuhi
    if jumlah_beasiswa_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

    print(f"\nData mahasiswa ke-{i}")

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    # Melewati mahasiswa yang IPK-nya kurang dari 3.00
    if ipk < 3.00:
        print("Status: Tidak memenuhi syarat IPK.")
        jumlah_tidak_memenuhi += 1
        continue

    penghasilan = float(
        input("Masukkan penghasilan orang tua per bulan (Rp): ")
    )

    # Menentukan jenis beasiswa
    if penghasilan <= 3000000:
        status = "Beasiswa Penuh"
        jumlah_beasiswa_penuh += 1

    elif penghasilan <= 5000000:
        status = "Beasiswa Sebagian"
        jumlah_beasiswa_sebagian += 1

    else:
        status = "Tidak Mendapatkan Beasiswa"
        jumlah_tidak_dapat += 1

    print("\nHasil seleksi mahasiswa:")
    print("Nama:", nama)
    print("IPK:", ipk)
    print("Status:", status)

    # Hentikan proses setelah mahasiswa ketiga mendapat
    # beasiswa penuh
    if jumlah_beasiswa_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

print("\n=== REKAPITULASI SELEKSI ===")
print("Penerima beasiswa penuh:", jumlah_beasiswa_penuh)
print("Penerima beasiswa sebagian:", jumlah_beasiswa_sebagian)
print("Tidak mendapatkan beasiswa:", jumlah_tidak_dapat)
print("Tidak memenuhi syarat IPK:", jumlah_tidak_memenuhi)
x = "wulan"

