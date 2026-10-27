print("=== PROGRAM BELANJA UDIN ===")

# Input data buku
harga_buku = float(input("Masukkan harga buku       : Rp"))
jumlah_buku = int(input("Masukkan jumlah buku      : "))

# Input data pulpen
harga_pulpen = float(input("Masukkan harga pulpen     : Rp"))
jumlah_pulpen = int(input("Masukkan jumlah pulpen    : "))

# Input data flashdisk
harga_flashdisk = float(input("Masukkan harga flashdisk  : Rp"))
jumlah_flashdisk = int(input("Masukkan jumlah flashdisk : "))

# Input uang yang dibayarkan
uang_dibayar = float(input("Masukkan uang yang dibayar 2: Rp"))

# Menghitung total masing-masing barang
total_buku = harga_buku * jumlah_buku
total_pulpen = harga_pulpen * jumlah_pulpen
total_flashdisk = harga_flashdisk * jumlah_flashdisk

# Total sebelum diskon
total_sebelum_diskon = total_buku + total_pulpen + total_flashdisk

# Diskon 10%
diskon = 0.10 * total_sebelum_diskon

# Harga setelah diskon
harga_setelah_diskon = total_sebelum_diskon - diskon

# Pajak 11%
pajak = 0.11 * harga_setelah_diskon

# Total setelah pajak
total_setelah_pajak = harga_setelah_diskon + pajak

# Kembalian
kembalian = uang_dibayar - total_setelah_pajak

# Menampilkan hasil
print("\n=== HASIL PERHITUNGAN ===")
print(f"a) Total harga buku              : Rp{total_buku:,.0f}")
print(f"b) Total harga pulpen            : Rp{total_pulpen:,.0f}")
print(f"c) Total harga flashdisk         : Rp{total_flashdisk:,.0f}")
print(f"d) Total sebelum diskon          : Rp{total_sebelum_diskon:,.0f}")
print(f"e) Besarnya diskon 10%           : Rp{diskon:,.0f}")
print(f"f) Harga setelah diskon          : Rp{harga_setelah_diskon:,.0f}")
print(f"g) Besarnya pajak 11%            : Rp{pajak:,.0f}")
print(f"h) Total setelah pajak           : Rp{total_setelah_pajak:,.0f}")
print(f"i) Uang kembalian                : Rp{kembalian:,.0f}")