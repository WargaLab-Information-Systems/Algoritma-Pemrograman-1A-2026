# Input total belanja
while True:
    try:
        input_belanja = input("Masukkan total belanja: ")

        # Mengecek apakah input kosong
        if input_belanja.strip() == "":
            print("Input tidak boleh kosong. Silakan masukkan total belanja.")
            continue

        total_belanja = int(input_belanja)

        # Mengecek angka negatif
        if total_belanja < 0:
            print("Total belanja tidak boleh negatif. Silakan masukkan angka yang benar.")
            continue

        break

    # Menangani input berupa teks
    except ValueError:
        print("Tolong jangan input dengan teks atau kalimat karena yang diminta adalah angka.")


# Total belanja awal
print("Total belanja awal: Rp", total_belanja)

# Pengecekan diskon
if total_belanja % 100000 == 0:
    total_bayar = 0
elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 50 // 100
elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 80 // 100
elif total_belanja >= 200000:
    total_bayar = total_belanja * 90 // 100
else:
    total_bayar = total_belanja

# Status poin
status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

# Hasil
print("Total harga akhir: Rp", total_bayar)
print("Status poin:", status_poin)