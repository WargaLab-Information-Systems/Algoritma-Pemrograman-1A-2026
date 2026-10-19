pin = int(input("masukkan pin 3 digit: "))
jam = int(input("masukkan jam kedatangan (0-23): "))

# memisahkan 3 digit
digit1 = pin//100
digit2 = (pin//10) % 10
digit3 = pin % 10 
print("digit pertama :", digit1)
print("digit kedua :", digit2)
print("digit ketiga :", digit3)

# menentukan status akses garasi
if pin % 5 == 0:
    if jam < 12:
        status = "garasi pagi terbuka"
    else:
        status = "garasi malam terbuka, lampu dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "garasi VIP terbuka khusus bos"
    else:
        status = "kode genap ditolak, alarm berbunyi!"
else:
    status = "akses ditolak sepenuhnya"

print("status akses garasi:", status)

# Ternary untuk CCTV
cctv = "mode malam merekam" if jam > 18 else "mode siang standby"
print("Status CCTV :", cctv)
print(f"Status CCTV : cctv")