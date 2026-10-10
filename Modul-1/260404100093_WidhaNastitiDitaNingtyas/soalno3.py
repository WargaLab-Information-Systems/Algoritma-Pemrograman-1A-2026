jarak = 100
konsumsi = 40
bensin = 1
sisaBensin = 1.5
hargaBahanBakar = 10000

jarakPP = jarak * 2
kebutuhanBahanBakar = jarakPP/ konsumsi
BahanBakarBeli = kebutuhanBahanBakar - sisaBensin
totalBiaya = BahanBakarBeli * hargaBahanBakar
jalanHanya10Km = 10/100 * jarak / konsumsi

print("Jarak pulang pergi yang harus ditempuh Dimas adalah", jarakPP, "km")
print("Kebutuhan bahan bakar untuk seluruh perjalanan adalah", kebutuhanBahanBakar, "liter")
print("Jumlah bahan bakar yang benar-benar harus dibeli Dimas", BahanBakarBeli, "liter")
print("Total biaya yang harus dikeluarkan DImas Rp.", totalBiaya)
print("total bensin yang dibutuhkan jika hanya jalan 10km yaitu", jalanHanya10Km, "liter" )

