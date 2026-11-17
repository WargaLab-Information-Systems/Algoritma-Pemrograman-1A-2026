
# Program Sistem Keamanan Pintu Garasi

# Input PIN dan jam kedatangan
pin = int(input("Masukkan 3 digit kode PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

# Memisahkan digit PIN secara matematis
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

# Menampilkan data PIN dan jam kedatangan
print("\n=== DATA AKSES GARASI ===")
print("PIN:", pin)
print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)
print("Jam kedatangan:", jam)

# Menentukan status akses pintu garasi
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
    status = "Akses Ditolak!"

# Ternary operator untuk status kamera CCTV
cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

# Menampilkan hasil
print("\n=== HASIL PEMERIKSAAN ===")
print("Status Akses:", status)
print("Status CCTV:", cctv)
