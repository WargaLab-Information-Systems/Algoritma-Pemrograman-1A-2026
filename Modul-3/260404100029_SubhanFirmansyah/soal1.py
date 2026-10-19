jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while 1:
    while 1:
        teks = input("Jarak penumpang (km): ")
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

        jarak = int(teks)                          
        if jarak < 0:
            print("Jarak negatif tidak valid, ulangi")
            continue
        break

    if jarak == 0:                                 
        break

    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah_penumpang % 5 == 0:                  
        tarif = tarif // 2
        print("Penumpang ke-", jumlah_penumpang, "mendapat diskon 50%")

    print("Tarif: Rp", tarif)

    total_pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("=== Ringkasan ===")
print("Jumlah penumpang :", jumlah_penumpang)
print("Total pendapatan : Rp", total_pendapatan)

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Jarak terjauh    :", jarak_terjauh, "km")
    print("Rata-rata jarak  :", rata_rata, "km")
else:
    print("Tidak ada penumpang")