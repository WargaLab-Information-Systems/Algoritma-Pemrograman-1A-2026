total_gaji = 0

for hari in range(1, 8):                           
    print("Hari ke-", hari,)

    while 1:
        teks = input("Jam lembur hari ini: ")
        if teks == "":
            print("Input tidak boleh kosong, ulangi")
            continue

        angka_valid = True
        jumlah_angka = 0
        posisi = 0
        for huruf in teks:                         
            posisi += 1
            if posisi == 1 and huruf == "-":       
                pass
            elif huruf >= "0" and huruf <= "9":
                jumlah_angka += 1
            else:
                angka_valid = False

        if angka_valid == False or jumlah_angka == 0:
            print("Input harus berupa bilangan bulat, ulangi")
            continue

        jam = int(teks)                            
        if jam < 0:
            print("Jam lembur tidak boleh negatif, ulangi")
            continue
        if jam == 5 or jam == 7:                   
            print("Jam lembur 5 dan 7 tidak sesuai ketentuan, ulangi")
            continue
        break

    while 1:
        teks = input("Shift malam? (1 = ya, 0 = tidak): ")
        if teks == "":
            print("Input tidak boleh kosong, ulangi")
            continue

        angka_valid = True
        jumlah_angka = 0
        posisi = 0
        for huruf in teks:
            posisi += 1
            if posisi == 1 and huruf == "-":
                pass
            elif huruf >= "0" and huruf <= "9":
                jumlah_angka += 1
            else:
                angka_valid = False

        if angka_valid == False or jumlah_angka == 0:
            print("Input harus berupa bilangan bulat, ulangi")
            continue

        shift = int(teks)
        if shift < 0:
            print("Input tidak boleh negatif, ulangi")
            continue
        if shift > 1:
            print("Masukkan 1 (ya) atau 0 (tidak), ulangi")
            continue
        break

    if jam == 0:
        UangLembur = 0
    elif jam <= 3:                                
        UangLembur = jam * 25000
    elif jam == 4:
        UangLembur = 100000
    elif jam == 6:
        UangLembur = 200000
    elif jam == 8:
        UangLembur = 300000
    else:                                          
        print("Jumlah lembur melebihi batas yang ditentukan, upah lembur tidak dihitung")
        UangLembur = 0

    if shift == 1:
        TambahanMalam = 50000
    else:
        TambahanMalam = 0

    GajiHariIni = 100000 + UangLembur + TambahanMalam

    print("Gaji pokok     : Rp 100000")
    print("Upah lembur    : Rp", UangLembur)
    print("Tambahan malam : Rp", TambahanMalam)
    print("Gaji hari ini  : Rp", GajiHariIni)
    print()

    total_gaji += GajiHariIni                        

print("===== GAJI MINGGUAN =====")
print("Total gaji satu minggu : Rp", total_gaji)