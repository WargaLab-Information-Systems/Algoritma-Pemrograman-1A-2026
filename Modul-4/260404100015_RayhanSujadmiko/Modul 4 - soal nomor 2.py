print("=== GAJI MINGGUAN KARYAWAN ===")
gaji_pokok = 100000
total_gaji = 0

# Perulangan FOR untuk memproses data selama 7 hari
for hari in range(1, 8):
    print(f"--- Hari ke-{hari} ---")
    upah_lembur = 0
    inputan = False
    cek_jam2 = 0.0 

    # Pengecekan inputan
    while inputan == False:
        cek_jam = input("Jam lembur (jam): ")
        if cek_jam == "":
            print("Input tidak boleh kosong, silakan ulangi.")
        else:
            apakah_angka = True
            for karakter in cek_jam:
                if karakter not in "0123456789":
                    apakah_angka = False
            
            if apakah_angka == False:
                print("Input harus berupa bilangan, silakan ulangi.")
            else:
                inputan2 = False
                while inputan2 == False:
                    cek_jam2 = float(cek_jam)
                    if cek_jam2 < 0:
                        print("Input tidak boleh negatif, silakan ulangi.")
                        inputan2 = True
                    elif cek_jam2 > 8:
                        print("Melebihi batas lembur yang ditentukan (maks. 8 jam), silakan ulangi.")
                        inputan2 = True
                    elif cek_jam2 == 5 or cek_jam2 == 7:
                        print("Jumlah jam lembur tersebut tidak valid berdasarkan ketentuan tarif, silakan ulangi.")
                        inputan2 = True
                    else:
                        inputan2 = True
                        inputan = True

    # Menentukan upah lembur
    if cek_jam2 == 0:
        upah_lembur = 0
    elif cek_jam2 >= 1 and cek_jam2 <= 3:
        upah_lembur = cek_jam2 * 25000
    elif cek_jam2 == 4:
        upah_lembur = 100000
    elif cek_jam2 == 6:
        upah_lembur = 200000
    elif cek_jam2 == 8:
        upah_lembur = 300000

    # Input dan percabangan untuk tambahan shift malam
    shift = input("Shift malam? (y/t): ")
    if shift == "y" or shift == "Y":
        tambahan_malam = 50000
    else:
        tambahan_malam = 0

    # Menghitung gaji harian
    gaji_hari = gaji_pokok + upah_lembur + tambahan_malam
    total_gaji = total_gaji + gaji_hari  
    print(f"Gaji hari ke-{hari}: Rp{gaji_hari:,}")

# Total gaji mingguan
print("===============================")
print(f"TOTAL GAJI MINGGUAN: Rp{total_gaji:,}")
