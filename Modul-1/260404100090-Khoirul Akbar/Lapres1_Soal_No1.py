saldoAwal = 2 * 100000

totalHargaBuku = 3 * 25000
totalHargaBulpen = 2 * 8000
totalHargaFlashdisk = 1 * 75000

totalHargaSebelumDiskon = totalHargaBuku + totalHargaBulpen + totalHargaFlashdisk

diskon = totalHargaSebelumDiskon * 10 / 100

totalHargaSesudahDiskon = totalHargaSebelumDiskon - diskon

ppn = totalHargaSesudahDiskon * 11 / 100

totalPembayaran = totalHargaSesudahDiskon + ppn

kembalian = saldoAwal - totalPembayaran

print("Total harga buku:", totalHargaBuku)
print("Total harga bulpen:", totalHargaBulpen)
print("Total harga flashdisk:", totalHargaFlashdisk)
print("Total harga sebelum diskon:", totalHargaSebelumDiskon)
print("Diskon:", diskon)
print("Total harga sesudah diskon:", totalHargaSesudahDiskon)
print("PPN:", ppn)
print("Total pembayaran:", totalPembayaran)
print("Kembalian:", kembalian)