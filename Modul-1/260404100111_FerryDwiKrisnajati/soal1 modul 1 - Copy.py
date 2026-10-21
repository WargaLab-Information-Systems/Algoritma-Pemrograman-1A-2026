uangUdin = 200000
totalBuku = 3 * 25000
totalPulpen = 2 * 8000
totalFlashdisk = 1 * 75000
subtotal = totalBuku + totalPulpen + totalFlashdisk
diskon = subtotal * 10 / 100
hargaSetelahDiskon = subtotal - diskon
pajak = hargaSetelahDiskon * 11 / 100
totalBayar = hargaSetelahDiskon + pajak
hargaSetelahDiskon = subtotal - diskon
totalBayar = hargaSetelahDiskon + pajak
kembalian = uangUdin - totalBayar
print("Total harga buku :" + str(totalBuku))
print("Total harga pulpen :" + str(totalPulpen))
print("Total harga flashdisk :" + str(totalFlashdisk))
print("Total harga seluruh barang sebelum diskon :" + str(subtotal))
print("Besarnya diskon 10% :" + str(diskon))
print("Harga barang setelah diskon :" + str(hargaSetelahDiskon))
print("Besarnya pajak 11% :" + str(pajak))
print("Total pembayaran setelah pajak :" + str(totalBayar))
print("Uang kembalian yang diterima Udin :" + str(kembalian))
