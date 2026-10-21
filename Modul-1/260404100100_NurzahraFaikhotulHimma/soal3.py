jarakSekaliJalan = 57
konsumsi = 40
sisaBBM = 1.5
hargaPerLiter = 10000

totalJarak = jarakSekaliJalan * 2
kebutuhanBBM = totalJarak / konsumsi
BBMdibeli = kebutuhanBBM - sisaBBM
totalBiaya = BBMdibeli * hargaPerLiter

print("Total jarak pulang-pergi :", totalJarak, "km")
print("Total kebutuhan BBM :", kebutuhanBBM, "liter")
print("BBM yang harus dibeli :", BBMdibeli, "liter")
print("Total biaya :", "Rp", int(totalBiaya))
