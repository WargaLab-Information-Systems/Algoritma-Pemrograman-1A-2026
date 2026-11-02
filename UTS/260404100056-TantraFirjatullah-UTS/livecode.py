tiket = [
    {"kelas": "Reguler", "harga": 40000},
    {"kelas":"VIP", "harga": 75000},
    {"kelas":"VVIP", "harga": 100000}
]

reguler = 0
vip = 0
vvip = 0
minuman = 0

print("1. Reguler(Rp40.000)")
print("2. VIP(Rp40.000)")
print("1. VVIP(Rp40.000)")

while True:
    while True:
        inputPengguna = int(input("Pilih Tiket (1-3): "))
        if inputPengguna > 3 or inputPengguna < 1:
            print("Tiket tidak valid.")
        else:
            break

    if inputPengguna == 0:
        break
    elif inputPengguna == 1:
        reguler += 1
        while True:
            inputMinuman = input("tambahan minuman seharga Rp10.000/tiket (Y/N): ")
            if inputMinuman == "y" or inputMinuman == "n":
                if inputMinuman == "y":
                    minuman += 1
                break
            else:
                print("salah")
                continue

    elif inputPengguna == 1:
        print("Sudah Include Minuman")
        vip += 1
    else:
        print("Sudah Include Minuman")
        vvip += 1



totalHargaReguler = reguler * tiket[0]["harga"]
totalHargaVIP = vip * tiket[1]["harga"]
totalHargaVVIP = vvip * tiket[2]["harga"]

totalTiket = reguler + vip + vvip
totalHargaTiket = totalHargaReguler + totalHargaVIP + totalHargaVVIP

diskon = 0

if totalTiket > 3:
    while True:
        member = input("Apakah Member Card ada(Y/N)? ").lower
        if member == "y" or member == "n":
            if member == "y":
                diskon = totalHargaTiket * (15/100)
            else:
                diskon = totalHargaTiket * (10/100)
            break
        else:
            continue

total = totalHargaTiket - diskon
print(f"Total Harga: {tiket}")
