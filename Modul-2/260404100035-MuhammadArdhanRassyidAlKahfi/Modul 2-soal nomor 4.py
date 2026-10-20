# Input PIN dan jam kedatangan

# Input PIN
while True:
    try:
        input_pin = input("Masukkan PIN 3 digit: ")

        # Mengecek apakah input kosong
        if input_pin.strip() == "":
            print("Input PIN tidak boleh kosong. Silakan masukkan PIN 3 digit.")
            continue

        pin = int(input_pin)

        # Mengecek angka negatif
        if pin < 0:
            print("PIN tidak boleh berupa angka negatif. Silakan masukkan PIN 3 digit.")
            continue

        # Mengecek apakah PIN terdiri dari 3 digit
        if pin < 100 or pin > 999:
            print("PIN harus terdiri dari 3 digit. Silakan masukkan PIN yang benar.")
            continue

        break

    except ValueError:
        print("Tolong jangan input dengan teks atau kalimat karena yang diminta adalah angka 3 digit.")


# Input jam
while True:
    try:
        input_jam = input("Masukkan jam kedatangan (0-23): ")

        # Mengecek apakah input kosong
        if input_jam.strip() == "":
            print("Input jam tidak boleh kosong. Silakan masukkan jam 0-23.")
            continue

        jam = int(input_jam)

        # Mengecek jam di luar rentang
        if jam < 0 or jam > 23:
            print("Jam harus berada di antara 0 sampai 23. Silakan masukkan jam yang benar.")
            continue

        break

    except ValueError:
        print("Tolong jangan input dengan teks atau kalimat karena yang diminta adalah angka.")


# Memisahkan digit
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

# Status akses pintu
if pin % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status = "Akses Ditolak Sepenuhnya"

# Status CCTV
cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

# Hasil
print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)
print("Status akses:", status)
print("Status CCTV:", cctv)