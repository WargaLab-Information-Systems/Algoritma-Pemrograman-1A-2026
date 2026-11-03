
baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

for i in range(1, baris + 1):
    print("Pemeriksaan pada baris ke-", i)

    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print("Lampu nomor", j, "dinyatakan mengalami gangguan.")
        else:
            print("Lampu nomor", j, "dinyatakan berfungsi normal.")

print("Pemeriksaan seluruh lampu telah selesai dilaksanakan.")
print("Selanjutnya, lakukan pemeriksaan terhadap sumber listrik utama taman.")
