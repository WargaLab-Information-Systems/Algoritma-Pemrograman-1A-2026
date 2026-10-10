kodeUser = int(input("Masukkan kode 3 digit: "))

if len(str(kodeUser)) != 3 or kodeUser < 0:
    print("Kode tidak valid, tidak dapat memproses kode.")
    exit()

jamKunjungan = int(input("Masukkan jam kunjungan: "))

if jamKunjungan > 23 or jamKunjungan < 0:
    print("Jam tidak valid.")
    exit()

digit = [
    kodeUser // 100,            # digit satu
    (kodeUser // 10) % 10,      # digit dua
    kodeUser % 10               # digit tiga
]

if (kodeUser % 5) == 0:
    if jamKunjungan < 12:
        statusAkses = "Garasi pagi terbuka."
    else:
        statusAkses = "Garasi malam terbuka. Lampu akan dinyalakan"
elif (kodeUser % 2) == 0:
    if (digit[0] + digit[2]) == digit[1]:
        statusAkses = "Garasi VIP terbuka khusus bos!"
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")
        exit()
else:
    print("Akses ditolak!")
    exit()

statusKamera = "Mode malam, merekam." if jamKunjungan > 18 else "Mode siang, standby."

print()
print(f"Digit pertama adalah: {digit[0]}")
print(f"Digit kedua adalah: {digit[1]}")
print(f"Digit ketiga adalah: {digit[2]}")
print(statusAkses)
print(statusKamera)
print()
