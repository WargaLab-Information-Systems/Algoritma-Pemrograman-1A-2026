# Program Diskon Supermarket "Koperasi Ndeso"

print("Jumlah Barang Yang Bu Siti Beli Sebanyak 3 Barang")

# Input harga barang 1
while True:
    teks = input("Masukkan harga barang 1: Rp")
    if teks == "":
        print("Peringatan: Input tidak boleh kosong!")
    else:
        try:
            harga1 = int(teks)
            if harga1 <= 0:
                print("Peringatan: Tidak boleh memasukkan angka minus atau 0!")
            else:
                break
        except ValueError:
            print("Peringatan: Tidak boleh memasukkan karakter selain bilangan bulat!")

# Input harga barang 2
while True:
    teks = input("Masukkan harga barang 2: Rp")
    if teks == "":
        print("Peringatan: Input tidak boleh kosong!")
    else:
        try:
            harga2 = int(teks)
            if harga2 <= 0:
                print("Peringatan: Tidak boleh memasukkan angka minus atau 0!")
            else:
                break
        except ValueError:
            print("Peringatan: Tidak boleh memasukkan karakter selain bilangan bulat!")

# Input harga barang 3
while True:
    teks = input("Masukkan harga barang 3: Rp")
    if teks == "":
        print("Peringatan: Input tidak boleh kosong!")
    else:
        try:
            harga3 = int(teks)
            if harga3 <= 0:
                print("Peringatan: Tidak boleh memasukkan angka minus atau 0!")
            else:
                break
        except ValueError:
            print("Peringatan: Tidak boleh memasukkan karakter selain bilangan bulat!")

# Menghitung total belanja
total = harga1 + harga2 + harga3
print("Total belanja awal: Rp", total)

# Mengecek diskon
if total % 100000 == 0:
    bayar = 0                      # Gratis
elif total % 50000 == 0:
    bayar = total * 50 // 100      # Diskon 50%
elif total % 10000 == 0:
    bayar = total * 80 // 100      # Diskon 20%
elif total >= 200000:
    bayar = total * 90 // 100      # Diskon 10%
else:
    bayar = total                  # Harga normal
print("Total harga akhir: Rp", bayar)

# Ternary operator
poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin:", poin)