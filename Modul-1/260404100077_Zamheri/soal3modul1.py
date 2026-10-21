jarak_sekali_jalan = 100      
konsumsi_bbm_per_liter = 40   
sisa_bbm_tangki = 1.5        
harga_bbm_per_liter = 10000   

# Total jarak adalah perjalanan pulang dan pergi
total_jarak_perjalanan = jarak_sekali_jalan * 2 

# Total BBM yang dihabiskan untuk keseluruhan perjalanan
kebutuhan_bbm_total = total_jarak_perjalanan / konsumsi_bbm_per_liter

# BBM yang benar-benar harus dibeli setelah dikurangi sisa di tangki
bbm_dibeli = kebutuhan_bbm_total - sisa_bbm_tangki

# Total biaya yang harus dibayar di SPBU
total_biaya_bbm = bbm_dibeli * harga_bbm_per_liter


print("--- Rincian Perjalanan Dimas ---")
print("Total jarak perjalanan (PP)  : {total_jarak_perjalanan} km")
print("Total kebutuhan bahan bakar  : {kebutuhan_bbm_total} liter")
print("Bahan bakar yang harus dibeli: {bbm_dibeli} liter")
print("Total biaya pembelian BBM    : Rp {total_biaya_bbm:,.0f}")