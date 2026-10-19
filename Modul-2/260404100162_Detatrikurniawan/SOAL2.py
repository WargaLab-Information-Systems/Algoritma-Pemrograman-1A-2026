total_awal = 0
nomor = 1
while True:
    harga = int(input(f"Harga barang ke-{nomor} (ketik 0 untuk selesai): Rp"))
    if harga == 0:
        break
    total_awal += harga
    nomor += 1
if total_awal > 0 and total_awal % 100000 == 0:
    persen_diskon = 100   # gratis total
elif total_awal > 0 and total_awal % 50000 == 0:
    persen_diskon = 50
elif total_awal > 0 and total_awal % 10000 == 0:
    persen_diskon = 20
elif total_awal >= 200000:
    persen_diskon = 10
else:
    persen_diskon = 0     
potongan = total_awal * persen_diskon / 100
total_bayar = total_awal - potongan
status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
print("\nSTRUK BELANJA SITI")
print(f"Total belanja awal : Rp{total_awal:,}".replace(",", "."))
print(f"Diskon             : {persen_diskon}%")
print(f"Total bayar        : Rp{int(total_bayar):,}".replace(",", "."))
print(f"Status poin        : {status_poin}")