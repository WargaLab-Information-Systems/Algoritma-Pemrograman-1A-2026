jumlah = 0
total = 0
terjauh = 0
total_jarak = 0

while True:
    print()
    print("Input data penumpang ke-", jumlah + 1)
    while True:
        teks = input("Jarak (km): ")

        # periksa tiap karakter: hanya angka 0-9 dan maksimal satu titik
        jumlah_titik = 0
        semua_valid = True
        ada_angka = False
        for karakter in teks:
            if karakter == ".":
                jumlah_titik += 1
            elif karakter in "0123456789":
                ada_angka = True
            else:
                semua_valid = False

        if teks == "":
            print("jarak tidak boleh kosong")
        elif teks[0] == "-":
            print("jarak tidak boleh negatif")
        elif not semua_valid or jumlah_titik > 1 or not ada_angka:
            print("jarak harus berupa angka dan boleh desimal")
        else:
            break

    jarak = float(teks)

    # jarak 0 = tanda berhenti
    if jarak == 0:
        break

    jumlah += 1
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    # penumpang kelipatan 5 diskon 50%
    if jumlah % 5 == 0:
        tarif = tarif / 2

    tarif = int(tarif + 0.5)   # pembulatan ke rupiah terdekat
    print("Tarif: Rp", tarif)
    total += tarif
    total_jarak += jarak

    if jarak > terjauh:
        terjauh = jarak

print()
if jumlah == 0:
    print("Belum ada penumpang yang diinput.")
else:
    print("Jumlah penumpang:", jumlah)
    print("Total pendapatan: Rp", total)
    print("Jarak terjauh:", terjauh, "km")
    print("Rata-rata jarak:", total_jarak / jumlah, "km")
print()