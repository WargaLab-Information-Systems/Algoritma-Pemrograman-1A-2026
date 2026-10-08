#  Perhitungan Pin Untuk Buka Pagar

# Input PIN
while True:
    teks = input("Masukkan PIN 3 digit: ")
    if teks == "":
        print("Peringatan: Input tidak boleh kosong!")
    else:
        try:
            pin = int(teks)
            if pin < 100 or pin > 999:
                print("Peringatan: PIN harus 3 digit (100 - 999)!")
            else:
                break
        except ValueError:
            print("Peringatan: Tidak boleh memasukkan karakter selain bilangan bulat!")

# Input jam
while True:
    teks = input("Masukkan jam kedatangan (0-23): ")
    if teks == "":
        print("Peringatan: Input tidak boleh kosong!")
    else:
        try:
            jam = int(teks)
            if jam < 0 or jam > 23:
                print("Peringatan: Jam harus antara 0 sampai 23!")
            else:
                break
        except ValueError:
            print("Peringatan: Tidak boleh memasukkan karakter selain bilangan bulat!")

# Memisahkan digit PIN
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)

# Menentukan akses
if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Dinyalakan")

elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")

else:
    print("Akses Ditolak")

# CCTV menggunakan ternary operator
cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
print(cctv)