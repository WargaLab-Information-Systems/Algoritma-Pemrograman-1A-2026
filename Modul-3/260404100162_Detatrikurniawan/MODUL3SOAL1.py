jumlah = 0
totaljarak = 0
jarakterjauh = 0
totalpendapatan = 0


while True:
    jarak = float(input("Masukkan anunya: "))
    if jarak == 0:
        break
    if jarak <0:
        print("Jarak gak valid, ULANG!")
        continue

    jumlah += 1

    if jarak <= 5:
       tarif = 3000
    elif jarak <= 15:
         tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
    if jumlah % 5 == 0:
       tarif = tarif * 0.5
       print("Kamu dapet Diskon 50%")

    totalpendapatan += tarif
    totaljarak += jarak
    if jarak > jarakterjauh:
       jarakterjauh = jarak
    print(f"Tarif penumpang ke-{jumlah}: Rp{tarif:.0f}")

print("Jumlah penumpang :", jumlah)
print(f"Total pendapatan : Rp{totalpendapatan:.0f}")
print("Jarak terjauh    :", jarakterjauh, "km")
if jumlah > 0:
    print("Rata-rata jarak  :", round(totaljarak / jumlah, 2), "km")
else:
    print("Rata-rata jarak  : 0 km")