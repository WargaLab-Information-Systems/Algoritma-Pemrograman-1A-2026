total_belanja = int(input("Masukkan total belanja: Rp"))

if total_belanja % 100000 == 0:
    diskon = 100
elif total_belanja % 50000 == 0:
    diskon = 50
elif total_belanja % 10000 == 0:
    diskon = 20
elif total_belanja >= 200000:
    diskon = 10
else:
    diskon = 0

besar_diskon = total_belanja * diskon / 100
total_bayar = total_belanja - besar_diskon

print("Total belanja : Rp", total_belanja)
print("Diskon        :", diskon, "%")
print("Besar diskon  : Rp", besar_diskon)
print("Total bayar   : Rp", total_bayar)

status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
print("Status poin   :", status_poin)
