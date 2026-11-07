while True:
    teks = input("Masukkan jumlah baris lampu: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isdigit():
        print("Input harus berupa bilangan bulat positif!")
    elif int(teks) <= 0:
        print("Jumlah baris harus lebih dari 0!")
    else:
        jumlah_baris = int(teks)
        break

while True:
    teks = input("Masukkan jumlah lampu setiap baris: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isdigit():
        print("Input harus berupa bilangan bulat positif!")
    elif int(teks) <= 0:
        print("Jumlah lampu harus lebih dari 0!")
    else:
        jumlah_lampu = int(teks)
        break

for baris in range(1, jumlah_baris + 1):
    print(f"\nPemeriksaan baris {baris}:")

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu {lampu}: mengalami gangguan.")
        else:
            print(f"Lampu {lampu}: berfungsi normal.")

print("\nPeriksa sumber listrik utama taman.")