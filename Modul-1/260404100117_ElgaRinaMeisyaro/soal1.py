uangUdin = 200000
totalBuku = 3 * 25000
totalPulpen = 2 * 8000
totalFlashdisk = 1 * 75000
subtotal = totalBuku + totalPulpen + totalFlashdisk
diskon = subtotal * 0.1
hargaSetelahDiskon = subtotal - diskon
pajak = hargaSetelahDiskon * 0.11
totalBayar = hargaSetelahDiskon + pajak
kembalian = uangUdin - totalBayar
print("Total harga buku :" + str(totalBuku) + chr(13) + "Total harga pulpen :" + str(totalPulpen) + chr(13) + "Total harga Flashdisk :" + str(totalFlashdisk) + chr(13) + "Total harga seluruh barang sebelum diskon :" + str(subtotal) + chr(13) + "Besarnya diskon 10% :" + str(diskon) + chr(13) + "Harga barang setelah diskon :" + str(hargaSetelahDiskon) + chr(13) + "Besarnya pajak 11% :" + str(pajak) + chr(13) + "Total pembayaran setelah pajak :" + str(totalBayar) + chr(13) + "Uang kembalian yang diterima Udin :" + str(kembalian), end='', flush=True)
