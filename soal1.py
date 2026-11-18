jumlah = 0
total_uang = 0
total_jarak = 0
terjauh = 0

jarak = int(input("Jarak (km), 0 untuk selesai: "))

while jarak != 0:
    if jarak < 0:
        print("Jarak tidak valid, ulangi!")
    else:
        jumlah = jumlah + 1
        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + 1000 * (jarak - 5)
        else:
            tarif = 13000 + 500 * (jarak - 15)

        if jumlah % 5 == 0:
            tarif = tarif // 2
            print("Diskon 50%")

        print("Tarif: Rp", tarif)
        total_uang = total_uang + tarif
        total_jarak = total_jarak + jarak

        if jarak > terjauh:
            terjauh = jarak

    jarak = int(input("Jarak (km), 0 untuk selesai: "))

print("Jumlah penumpang :", jumlah)
print("Total pendapatan : Rp", total_uang)
print("Jarak terjauh    :", terjauh, "km")
if jumlah > 0:
    print("Rata-rata jarak  :", total_jarak / jumlah, "km")