while True:
    baris = input("Berapa Baris Lampu? ")
    huruf = baris != ""
    for karakter in baris:
        if karakter < "0" or karakter > "9":
            huruf = False
    if huruf == True:
        baris = int(baris)
        break
    print("Dilarang memasukkan input Angka Minus(-), Input Yang selain di suruh, (Contoh Yang Benar -----> 3)")

while True:
    jumlah = input("Berapa Jumlah Lampu dibaris Tersebut? ")
    huruf = jumlah != ""
    for karakter in jumlah:
        if karakter < "0" or karakter > "9":
            huruf = False
    if huruf == True:
        jumlah = int(jumlah)
        break
    print("Dilarang memasukkan input Angka Minus(-), Input Yang selain di suruh, (Contoh Yang Benar -----> 3)")

normal = 0
gangguan = 0

for i in range(1, baris + 1):
    print("\n==== Baris", i, " ====")
    for j in range(1, jumlah + 1):
        if j % 3 == 0:
            gangguan += 1
            print("Lampu ", j, " ---> Mengalami Gangguan")
        else:
            normal += 1
            print("Lampu ", j, " ---> Normal")

if gangguan > 0 and normal > 0:
    print("\n==== Periksa Sumber Listrik Taman ====")
else:
    print("\n==== Lampu Normal Semua ====")