
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for baris in range(1, jumlah_baris + 2):
    print(f"\nPemeriksaan baris ke-{baris}")

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu {lampu}: Mengalami gangguan")
        else:
            print(f"Lampu {lampu}: Berfungsi normal")

print("\nPeriksa sumber listrik utama taman.")
