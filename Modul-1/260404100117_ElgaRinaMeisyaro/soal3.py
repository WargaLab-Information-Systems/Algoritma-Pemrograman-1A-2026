jarak_pergi = 100
total_kebutuhan_bahanbakar = 40
harga_bahan_bakar = 10000
total_sisa_bahanbakar = 1.5

total_jarak = jarak_pergi*2
total_kebutuhan_bahanbakar = total_jarak / total_kebutuhan_bahanbakar
bahanbakar_dibeli = total_kebutuhan_bahanbakar - total_sisa_bahanbakar
total_biaya = bahanbakar_dibeli * harga_bahan_bakar
print("Jaraknya adalah", total_jarak)
print(total_kebutuhan_bahanbakar)
print(bahanbakar_dibeli)
print(total_biaya)