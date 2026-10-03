jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga = 10000

total_jarak = jarak * 2
kebutuhan = total_jarak / konsumsi
harus_beli = kebutuhan - sisa_bensin
biaya = harus_beli * harga

print("Total jarak pulang-pergi:", total_jarak, "km")
print("Kebutuhan bensin:", kebutuhan, "liter")
print("Bensin yang harus dibeli:", harus_beli, "liter")
print("Total biaya: Rp", biaya)