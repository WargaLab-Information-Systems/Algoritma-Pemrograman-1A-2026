jarak_satu_arah = 100        # kilometer
konsumsi_bbm = 40            # kilometer per liter
sisa_bensin = 1.5            # liter
harga_per_liter = 10000      # rupiah

jarak_pulang_pergi = jarak_satu_arah * 2
kebutuhan_bbm_total = jarak_pulang_pergi / konsumsi_bbm
bbm_yang_harus_dibeli = kebutuhan_bbm_total - sisa_bensin
total_biaya = bbm_yang_harus_dibeli * harga_per_liter

print("Total jarak pulang-pergi      : ",jarak_pulang_pergi,"km")
print("Total kebutuhan bahan bakar   : ",kebutuhan_bbm_total,"liter")
print("Bahan bakar yang harus dibeli : ",bbm_yang_harus_dibeli, "liter")
print("Total biaya bahan bakar       : Rp",total_biaya)                                                                                                                                                                                                      