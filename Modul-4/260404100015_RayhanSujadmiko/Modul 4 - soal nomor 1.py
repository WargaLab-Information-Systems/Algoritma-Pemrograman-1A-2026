print("=== PEMERIKSAAN LAMPU TAMAN ===")

# Jumlah Baris Lampu
baris = 0
inputan = False

while inputan == False:
    baris_lampu = input("Masukkan jumlah baris lampu: ")
    if baris_lampu == "":
        print("Input tidak boleh kosong, silakan ulangi.")
    else:
        apakah_angka = True
        for karakter in baris_lampu:
            if karakter not in "0123456789":
                apakah_angka = False
                
        if apakah_angka == False:
            print("Input harus berupa bilangan bulat positif, silakan ulangi.")
        else:
            baris = int(baris_lampu)
            inputan = True

# Jumlah Lampu Tiap Baris
lampu = 0
inputan = False

while inputan == False:
    jumlah_lampu = input("Masukkan jumlah lampu tiap baris: ")
    if jumlah_lampu == "":
        print("Input tidak boleh kosong, silakan ulangi.")
    else:
        apakah_angka = True
        for karakter in jumlah_lampu:
            if karakter not in "0123456789":
                apakah_angka = False
                
        if apakah_angka == False:
            print("Input harus berupa bilangan bulat positif, silakan ulangi.")
        else:
            lampu = int(jumlah_lampu)
            inputan = True

print()

# Pemeriksaan Tiap Lampu (Nested Loop)
for a in range(1, baris + 1):
    print(f"--- Baris ke-{a} ---")
    for b in range(1, lampu + 1):
        if b % 3 == 0:
            print(f"Lampu {b}: mengalami gangguan")
        else:
            print(f"Lampu {b}: berfungsi normal")
    print()
            
print("Seluruh lampu telah diperiksa.")
print("Silakan periksa sumber listrik utama taman.")
