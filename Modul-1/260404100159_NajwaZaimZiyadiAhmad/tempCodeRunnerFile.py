# Program Menghitung Kebutuhan Bahan Bakar Dimas

print("=== PROGRAM MENGHITUNG BAHAN BAKAR ===")

# Input data
jarak = float(input("Masukkan jarak satu arah (km)       : "))
konsumsi = float(input("Masukkan konsumsi motor (km/liter) : "))
sisa_bensin = float(input("Masukkan sisa bensin (liter)        : "))
harga_bensin = float(input("Masukkan harga bensin per liter     : Rp"))

# Menghitung total jarak pulang-pergi
total_jarak = jarak * 2

# Menghitung total kebutuhan bensin
total_bensin = total_jarak / konsumsi

# Menghitung bensin yang harus dibeli
bensin_dibeli = total_bensin - sisa_bensin

# Menghitung total biaya
total_biaya = bensin_dibeli * harga_bensin

# Menampilkan hasil
print("\n=== HASIL PERHITUNGAN ===")
print(f"Total jarak pulang-pergi : {total_jarak:.2f} km")
print(f"Total kebutuhan bensin   : {total_bensin:.2f} liter")
print(f"Bensin yang harus dibeli : {bensin_dibeli:.2f} liter")
print(f"Total biaya bensin       : Rp{total_biaya:,.0f}")