jumlahBaris = int(input("Jumlah baris lampu: "))
jumlahLampuPerBaris = int(input("Jumlah lampu tiap baris: "))

for nomorBaris in range(1, jumlahBaris + 1):
    print("Baris", nomorBaris)
    for nomorLampu in range(1, jumlahLampuPerBaris + 1):
        if nomorLampu % 3 == 0:
            print("Lampu", nomorLampu, "mengalami ganguan")
        else:
            print("Lampu", nomorLampu, "berfungsi normal")

print("Periksa sumber listrik utama taman!")
