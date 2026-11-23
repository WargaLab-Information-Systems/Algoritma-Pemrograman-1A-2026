# Menyimpan total gaji selama 7 hari
total_gaji = 0

# Menghitung gaji dari hari pertama sampai hari ketujuh
for hari in range(1, 8):
    print("Hari ke-", hari)

    # Menentukan gaji pokok per hari
    gaji_pokok = 100000

    # Memasukkan jumlah jam lembur
    jam_lembur = int(input("Masukkan jam lembur: "))

    # Memeriksa apakah jam lembur sesuai ketentuan
    while jam_lembur not in [0, 1, 2, 3, 4, 6, 8]:
        if jam_lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan.")
            print("Upah lembur tidak dihitung.")
        else:
            print("Jam lembur tidak sesuai ketentuan.")

        # Meminta pengguna memasukkan ulang jam lembur
        jam_lembur = int(input("Masukkan ulang jam lembur: "))

    # Menghitung upah lembur 1 sampai 3 jam
    if jam_lembur >= 1 and jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    # Memasukkan informasi shift malam
    shift = input("Bekerja shift malam? (ya/tidak): ")

    # Menambahkan upah shift malam jika bekerja
    if shift == "ya":
        tambahan = 50000
    else:
        tambahan = 0

    # Menghitung gaji harian
    gaji_harian = gaji_pokok + upah_lembur + tambahan

    # Menambahkan gaji harian ke total gaji
    total_gaji = total_gaji + gaji_harian

    # Menampilkan gaji harian
    print("Gaji hari ini: Rp", gaji_harian)
    print()

# Menampilkan total gaji selama 7 hari
print("Total gaji selama 7 hari: Rp", total_gaji)