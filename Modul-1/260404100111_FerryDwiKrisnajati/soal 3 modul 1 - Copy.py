jarak_pergi = 100
keperluan_bahan_bakar = 40
sisa_bahan_bakar = 1.5
harga_bahan_bakar = 10000

total_jarak = jarak_pergi * 2
total_bahan_bakar = total_jarak / keperluan_bahan_bakar
bahan_bakar_dibeli = total_bahan_bakar - sisa_bahan_bakar
total_biaya = bahan_bakar_dibeli * harga_bahan_bakar

print ("total_jarak :" ,total_jarak , "km")
print ("total_bahan_bakar :" ,total_bahan_bakar , "liter")
print ("bahan_bakar_dibeli :," ,bahan_bakar_dibeli , "liter")
print ("total_biaya :" ,total_biaya , "rupiah")