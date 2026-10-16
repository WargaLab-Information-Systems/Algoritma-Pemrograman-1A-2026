jarak = 100
bensin = 40 
bensin_sisa = 1.5
harga_bensin = 10000

total_jarak = jarak * 2
print("jarak yang ditempuh dimas adalah =",total_jarak,"kilo mater")

kebutuhan_bensin = total_jarak / bensin
print("konsumsi bensin = ", bensin, "km perliter")
print("bensin yang dibutuhkan=",kebutuhan_bensin,"liter")


beli_bensin = kebutuhan_bensin - bensin_sisa
print("jumlah bensin yang harus di beli dimas=",beli_bensin)

total_belibensin = harga_bensin * beli_bensin
print("total biaya dimas untuk beli bensin=",total_belibensin)