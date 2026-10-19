#IF-ELSE Command
#nilai = int(input("Masukkan nilai pre test  and :"))

#if nilai <=80 :
#   print("selamat, anda lulus pre-test")
#else:
#    print("maaf, anda tidak luli pre-test")


# roda =int(input("masukkan jumlah roda kendaraan :"))

# if roda == 2 :
#     print("kendaraan ini adalah sepeda motor")
# elif roda == 4 :
#     print("kendaraan ini adalah mobil")
# elif roda == 3 :
#     print("kendaraan ini adalah bajaj")
# else:
#     print("kendaraan ini adalah truk")

#NEstED IFS Command
# member = input("Apakah anda seorang member? (y/n): ")
# if member == "y":
#     belanja = int(input("masukkan jumlah belanja anda: "))
#     if belanja >=500:
#         print("selamat,  anda mendapatkan diskon 10%")
#     elif belanja  >=1000:
#         print("selamat,  anda mendapatkan diskon 20%")
#     else:
#         print("maaf, anda tidak mendapatkan diskon")
# else:
#     print("maaf, anda bukan member, tidak mendapatkan diskon")

# suhu = float(input("masukan suhu tubuh anda (cecius):"))

# status = "puanas" if suhu < 39.5 else "Hipotermia"
# print("status suhu tubuh anda adalah:", status)
pembeli = input("apakah anda ingin membeli dengan jumlah lebih dari 200000 ?(y/n): ")
if pembeli == "n" :
    belanja =int(input("masukan jumlah belanjaan anda: "))
    if belanja >=100:
        print("selamat, diskon belanjaan anda gratis")
    elif belanja >=50:
        print("selamat, diskon belanjaan anda 50%")
    elif belanja >=10:
        print("selamat, diskon belanjaan anda 20%")
    elif belanja >=200:
        print("selamat, diskon belanjaan anda 10%")
    else:
        print("maaf, anda tidak mendapatkan diskon")
else:
    print("maaf, anda telah melewati jumlah harga, tidak mendapatkan diskon")
# Program Diskon Belanja Siti
