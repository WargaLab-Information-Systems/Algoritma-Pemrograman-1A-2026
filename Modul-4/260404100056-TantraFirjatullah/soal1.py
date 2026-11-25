jumlahBaris = int(input("Masukkan jumlah baris lampu: "))
jumlahLampu = int(input("Masukkan jumlah lampu/baris: "))

for i in range(1, jumlahBaris + 1):
    for k in range(1, jumlahLampu + 1):
        if k % 3 == 0:
            print(f"Lampu ke-{k}, baris ke-{i} mengalami gangguan")

print("lakukan pengecekan sumber listrik utama!")
