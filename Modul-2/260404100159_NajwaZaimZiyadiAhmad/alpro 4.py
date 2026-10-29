
pin = int(input("Masukkan 3 digit kode PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        statusAkses = "Garasi Pagi Terbuka"
    else:
        statusAkses = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if (digit1 + digit3) == digit2:
        statusAkses = "Garasi VIP Terbuka Khusus Bos"
    else:
        statusAkses = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    statusAkses = "Akses Ditolak"

statusCCTV = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("\n--- LAPORAN AKSES MARKAS CIA ---")
print("PIN Masuk       :", pin)
print("Digit Pertama   :", digit1)
print("Digit Kedua     :", digit2)
print("Digit Ketiga    :", digit3)
print("Jam Kedatangan  :", jam)
print("Status Akses    :", statusAkses)
print("Status CCTV     :", statusCCTV)