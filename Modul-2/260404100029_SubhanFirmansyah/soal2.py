
while True:
    total = input("Masukkan total belanja awal Siti (Rp): ")
    
    if total == "" or total.isspace():
        print("Input tidak boleh kosong! Silakan masukkan angka.")
        continue
    
    try:
        total = float(total)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar (bukan huruf).")
        continue
        
    if total < 0:
        print("Maaf, tidak bisa memasukkan bilangan negatif. Tolong input ulang.")
        continue
    break

if total % 100000 == 0:
    diskonPersen = total
    totalBayar = 0
elif total % 50000 == 0:
    diskonPersen = total * 50 / 100
    totalBayar = total - diskonPersen
elif total % 10000 == 0:
    diskonPersen = total * 20 / 100
    totalBayar = total - diskonPersen
elif total >= 200000:
    diskonPersen = total * 10 / 100
    totalBayar = total - diskonPersen
else:
    diskonPersen = 0
    totalBayar = total

# operator Ternary
statusPoin = "Poin Bertambah" if totalBayar > 0 else "Tidak Ada Poin"
 
print("\n--- RINCIAN BELANJA SITI ---")
print("Total Belanja Awal : Rp", total)
print("Total Harga Akhir  : Rp", totalBayar)
print("Status Poin        :", statusPoin)