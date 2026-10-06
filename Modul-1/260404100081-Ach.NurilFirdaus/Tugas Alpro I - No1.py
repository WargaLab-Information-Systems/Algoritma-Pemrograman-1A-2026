print("Sisa Uang Recehmu Adalah")
uang = 250.0
print(uang)
print("Masukkan Jumlah Buku")
buku = int(input())
buku = buku * 25.0
print("Masukkan Jumlah Pulpen")
pulpen = int(input())
pulpen = pulpen * 8.0
print("Masukkan Jumlah Flashdisk")
flashdisk = int(input())
flashdisk = 75.0
print("ini total belanja anda")
total = buku + pulpen + flashdisk
print(total)
print("selamat anda  mendapatkan diskon")
diskon = uang - total * float(10) / 100
print(diskon)
print("rayakan kebahagiaan anda")
print("eiitss, jangan seenang dulu")
print("anda masih dikenakan pajak")
pajak = float(diskon * 11) / 100
print("ini total harganya")
print(pajak)
