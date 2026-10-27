jarak_pergi = 100
jarak_pulang = 100
konsumsi_bensin = 40
sisa_bensin = 1.5
harga_bensin = 10000

total_jarak = jarak_pergi + jarak_pulang
kebutuhan_bensin = total_jarak / konsumsi_bensin
bensin_dibeli = kebutuhan_bensin - sisa_bensin
total_biaya = bensin_dibeli * harga_bensin

print("Total jarak perjalanan :", total_jarak, "km")
print("Kebutuhan bensin       :", kebutuhan_bensin, "liter")
print("Bensin yang dibeli     :", bensin_dibeli, "liter")
print("Total biaya             : Rp", total_biaya)