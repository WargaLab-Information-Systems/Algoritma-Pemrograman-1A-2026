jarak_satu_arah = 100  # dalam km 
konsumsi_bbm = 40       # 1 liter untuk 40 km 
sisa_bensin = 1.5       # dalam liter 
harga_per_liter = 10000 # dalam Rupiah 
 
# 1. Menghitung total jarak perjalanan pulang-pergi 
total_jarak = jarak_satu_arah * 2 
 
# 2. Menghitung total kebutuhan bahan bakar seluruh perjalanan 
total_kebutuhan_bbm = total_jarak / konsumsi_bbm 
 
# 3. Menghitung jumlah bahan bakar yang harus dibeli 
bbm_yang_dibeli = total_kebutuhan_bbm - sisa_bensin 
 
# 4. Menghitung total biaya bahan bakar yang harus dikeluarkan 
total_biaya = bbm_yang_dibeli * harga_per_liter 
 
# Menampilkan hasil perhitungan 
print("=== PERHITUNGAN KEBUTUHAN PERJALANAN DIMAS ===") 
print(f"Total jarak pulang-pergi : {total_jarak} km") 
print(f"Total kebutuhan bensin   : {total_kebutuhan_bbm} liter") 
print(f"Bensin yang harus dibeli : {bbm_yang_dibeli} liter") 
print(f"Total biaya bensin       : {total_biaya}") 