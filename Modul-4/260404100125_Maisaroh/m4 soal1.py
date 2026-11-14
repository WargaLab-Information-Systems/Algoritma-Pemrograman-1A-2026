baris = int(input("masukkan jumlah baris lampu: "))
lampu = int(input("masukkan jumlah lampu pada setiap baris: "))

for i in range(1, baris + 3):
    print(f"baris ke-{i}")
    for j in range(1, lampu + 1):
        if j % 3 == 0:
            print(f"  lampu {j}: mengalami gangguan")
        else:
            print(f"  lampu {j}: berfungsi normal")

print("periksa sumber listrik utama taman!")