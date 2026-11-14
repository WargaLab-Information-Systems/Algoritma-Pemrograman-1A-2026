# Program Menghitung Kebutuhan Bahan Bakar Dimas

# Data yang diketahui
jarak_pergi = 100          # jarak rumah ke rumah keluarga (km)
konsumsi = 40              # konsumsi bahan bakar mobil (km/liter)
sisa_bensin = 1.5          # sisa bensin di tangki (liter)
harga_bensin = 10000       # harga bensin per liter (Rp)

# Menghitung total jarak pulang-pergi
total_jarak = jarak_pergi * 2

# Menghitung total kebutuhan bahan bakar
kebutuhan_bensin = total_jarak / konsumsi

# Menghitung bensin yang harus dibeli
bensin_dibeli = kebutuhan_bensin - sisa_bensin

# Menghitung total biaya
total_biaya = bensin_dibeli * harga_bensin

# Menampilkan hasil
print("=== Perhitungan Kebutuhan Bahan Bakar Dimas ===")
print("Jarak pulang-pergi :", total_jarak, "km")
print("Kebutuhan bensin :", kebutuhan_bensin, "liter")
print("Sisa bensin di tangki :", sisa_bensin, "liter")
print("Bensin yang harus dibeli :", bensin_dibeli, "liter")
print("Harga bensin per liter : Rp", harga_bensin)
print("Total biaya pembelian : Rp", total_biaya)