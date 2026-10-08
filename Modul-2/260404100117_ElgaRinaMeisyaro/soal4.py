pin = int(input("Masukkan PIN 3 digit: "))
jam = float(input("Masukkan jam kedatangan: "))

# Memisahkan digit PIN
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)

# Menentukan akses
if pin % 5 == 0:
    if jam < 12.00:
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
cctv = "Mode Malam Merekam" if jam > 18.00 else "Mode Siang Standby"
print(cctv)
