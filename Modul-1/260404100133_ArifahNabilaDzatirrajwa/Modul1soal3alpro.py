jarak = 100
konsumsi_bahan_bakar = 40
sisa_bensin = 1.5
harga_bensin = 10000

jarak_pulang_pergi = jarak * 2
kebutuhan_bensin = jarak_pulang_pergi / konsumsi_bahan_bakar
bensin_beli = kebutuhan_bensin - sisa_bensin
total_biaya = bensin_beli * harga_bensin

print("Total jarak pulang-pergi =", jarak_pulang_pergi, "km")
print("Total kebutuhan bahan bakar =", kebutuhan_bensin, "liter")
print("Bahan bakar yang harus dibeli =", bensin_beli, "liter")
print("Total biaya bahan bakar = Rp", total_biaya)
