jumlahPenumpang = 0
totalpendapatan = 0
jarakTerjauh = 0
totalJarak = 0

# perhitungannya
while True:
    jarak = float(input("masukkan jarak penumpang (km): "))
    if jarak == 0:
        break
    if jarak < 0:
        print("jarak tidak valid, silahkan masukkan kembali")
        continue
    jumlahPenumpang += 1
    totalJarak += jarak

    if jarak <= 5:
        tarif = 3000
        print("tarif:", tarif)
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
        print("tarif:", tarif)
    else:
        tarif = 13000 + (jarak - 15) * 500
        print("tarif:", tarif)

    if jumlahPenumpang % 5 == 0:
        tarif = tarif * 0.5
        print("mendapat diskon 50%")
    
    totalJarak += tarif
    if jarak > jarakTerjauh:
        jarakTerjauh = jarak

    print("tarif yang harus dibayar: Rp", tarif)
    print("total penumpang:", jumlahPenumpang)
    print("total pendapatan: Rp", totalpendapatan)
    print("jarak terjauh:", jarakTerjauh, "km")
    
    if jumlahPenumpang > 0:
        ratarata = totalJarak / jumlahPenumpang
        print("rata rata jarak:", ratarata, "km")
    else:
        print("rata rata jarak: 0 km")