while True :
    pin = input("masukkan PIN 3 digit :")
    if pin == "" or pin.isspace():
        print("input tidak boleh kosong! Silahkan masukkan angka")
        continue
    try :
        pin = int(pin)
    except ValueError :
        print("Input tidak valid. Harap masukkan angka yang benar (bukan huruf).")
        continue   
    if  pin < 0 :
        print("maaf tidak boleh memasukkan angka negatif, silahkan input ulang")
        continue
    break

while True :
    jam = input("masukkan jam kedatangan anda (0-23) :")
    if jam == "" or jam.isspace():
        print("input tidak boleh kosong! Silahkan masukkan angka")
        continue
    try :
        jam = int(jam)
    except ValueError :
        print("Input tidak valid. Harap masukkan angka yang benar (bukan huruf).")
        continue
    if jam < 0:
        print("maaf tidak boleh memasukkan angka negatif, silahkan input ulang")
        continue
    break

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0 :
    if jam < 12 :
        status = "garasi pagi telah terbuka"
    else :
        status = "garasi malam telah terbuka, lampu dinyalakan"
elif pin % 2 == 0 :
    if digit1 + digit3 == digit2 :
        status = "garasi VIP telah terbuka untuk BOS"
    else :
        status = "kode genap ditolak, alarm berbunyi"
else :
    status = "kode ditolak sepenuhnya"

# operator ternary
cctv = "mode malam terbuka" if jam > 18 else "mode siang stanby"
print("\n--- RINCIAN KONDISI GARASI ---")
print("digit pertama :", digit1)
print("digit kedua   :", digit2)
print("digit ketiga  :", digit3)
print("status akses  :", status)
print("status CCTV   :", cctv)