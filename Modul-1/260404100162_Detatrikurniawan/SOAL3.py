jarak=100
konsumsi_bahan_bakar=40
sisa_bahan_bakar=1.5
harga_bahan_bakar=10000

total_jarak=jarak*2
total_konsumsi_bahan_bakar=total_jarak/konsumsi_bahan_bakar
harus_beli=konsumsi_bahan_bakar-sisa_bahan_bakar
total_biaya=harus_beli*harga_bahan_bakar

print("total_jarak_pulang-pergi:", total_jarak, "km")
print("total_konsumsi_bahan_bakar:", total_konsumsi_bahan_bakar)
print("harus_beli:", harus_beli)
print("total_biaya:", total_biaya)