pin = int(input("Masukkan 3 digit kode PIN: "))
while pin < 100 or pin > 999:
    print("PIN harus tepat 3 digit (100-999)!")
    pin = int(input("Masukkan 3 digit kode PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))
while jam < 0 or jam > 23:
    print("Jam harus antara 0 sampai 23!")
    jam = int(input("Masukkan jam kedatangan (0-23): "))
digit1 = pin // 100          
digit2 = (pin // 10) % 10    
digit3 = pin % 10            

if pin % 5 == 0:
    if jam < 12:
        status_akses = "Garasi Pagi Terbuka"
    else:
        status_akses = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status_akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        status_akses = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status_akses = "Akses Ditolak"

status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("\n===== HASIL PEMERIKSAAN =====")
print(f"PIN            : {pin}")
print(f"Digit pertama  : {digit1}")
print(f"Digit kedua    : {digit2}")
print(f"Digit ketiga   : {digit3}")
print(f"Jam kedatangan : {jam}")
print(f"Status akses   : {status_akses}")
print(f"Status CCTV    : {status_cctv}")