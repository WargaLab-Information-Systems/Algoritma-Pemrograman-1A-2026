reguler = 40000
vip = 75000
vvip = 100000
jumlahTiket = 0

while True:
    jenisTiket = input("Masukkan Jenis Tiket (reguler, vip, vvip) = ")
    print("Jenis Tiket Yang Anda Beli =", jenisTiket)
    jumlahTiket += 1

    while True:
        if jenisTiket == "reguler":
            minum = "Apakah anda ingin beli minum? "
            if minum == "Y" or "y":
                harga = reguler + 10000
        if jenisTiket == "vip":
            print("Selamat anda mendapat minuman gratis")
            if jumlahTiket > 3:
                member = input("Apakah anda member?(y/n) ")
                if member == "y" or "Y":
                    harga /= 0.15
                if member == "n" or "N":
                    harga /= 0.10
                    break
        elif jenisTiket == "vvip":
            print("Selamat anda mendapat minuman gratis")
            if jumlahTiket > 3:
                member = input("Apakah anda member?(y/n) ")
                if member == "y" or "Y":
                    harga /= 0.15
                if member == "n" or "N":
                    harga /= 0.10
                    break

        while True:
            print("Total Harga = ", harga)
            bayar = int(input("tolong bayar = "))
            if harga > bayar:
                break
            print("MAAF UANG ANDA KURANG")         



"""

catatan penjelasan

ketika saya input kan reguler, itu akan langsung menuju print jenis tiker, dan total harga nya, setelah itu akan disuruh inpukan pembayaran nya, jika pembayaran nya itu kurang
maka akan di suruh untuk input lagi, untuk yang vip dan vvip belum selesai
"""