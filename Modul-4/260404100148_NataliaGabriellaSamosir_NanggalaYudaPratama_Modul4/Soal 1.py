
# Program Pemeriksaan Lampu Taman Kota

print("=== PEMERIKSAAN LAMPU TAMAN KOTA ===")

# Input jumlah baris dan lampu
baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

while baris <= 0 or jumlah_lampu <= 0:
    print("Jumlah baris dan lampu harus berupa bilangan bulat positif!")
    baris = int(input("Masukkan jumlah baris lampu: "))
    jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for a in range(1, baris + 1):
    print("\nBaris ke-", a)

    for d in range(1, jumlah_lampu + 1):
        if d % 3 == 0:
            print("Lampu", d, "mengalami gangguan")
        else:
            print("Lampu", d, "berfungsi normal")

print("\nPeriksa sumber listrik utama taman!")
