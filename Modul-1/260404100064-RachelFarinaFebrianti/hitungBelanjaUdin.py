uang = 200000
buku = 3 * 25000
pulpen = 2 * 8000
flashdisk = 1 * 75000
total = buku + pulpen + flashdisk
diskon = total * 0.1
setelahDiskon = total - diskon
pajak = buku * 0.11
totalBayar = setelahDiskon + pajak
kembalian = uang - totalBayar
print("a) Total harga buku: Rp" + str(buku))
print("b) Total harga pulpen: Rp" + str(pulpen))
print("c) Total harga flashdisk: Rp" + str(flashdisk))
print("d) Total harga sebelum diskon: Rp" + str(total))
print("e) Diskon: Rp" + str(diskon))
print("f) Harga setelah diskon: Rp" + str(setelahDiskon))
print("g) Pajak: Rp" + str(pajak))
print("h) Total pembayaran: Rp" + str(totalBayar))
print("i) Uang kembalian: Rp" + str(kembalian))
