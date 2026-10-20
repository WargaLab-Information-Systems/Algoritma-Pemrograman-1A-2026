jumlahPenumpang = 0
totalPendapatan = 0
jarakTerjauh = 0
totalJarak = 0

print("==== MASUKKAN JARAK PENUMPANG ====")
while True:

    # akan diulang kalau kosong/bukan angka/negatif 
    while True:
        jarak = input("Masukkan Jarak(KM) = ")
        valid = jarak != ""
        for karakter in jarak:
            if karakter < "0" or karakter > "9":
                valid = False
        if valid == True:
            jarak = int(jarak)
            break
        print("Maaf, jarak tidak valid, mohon ulangi inputnya")

    if jarak == 0:
        break

# setiap input jarakk di atas angka 0 itu akan menambah 1 di jumlah penumpangnya
    jumlahPenumpang += 1

# pengkondisian setiap jarak
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

# penjumlahan diskon
    if jumlahPenumpang % 5 == 0:
        tarif *= 0.5

    totalPendapatan += tarif 
    # sama dengan totalPendapatan = totalPendapatan + tarif
    totalJarak += jarak
    # sama dengan totalJarak = totalJarak + jarak
    if jarak > jarakTerjauh:
        jarakTerjauh = jarak

print("\n==== RATA - RATA JARAK PENUMPANG ====")
if jumlahPenumpang > 0:
    print("Rata - Rata Jarak = ", totalJarak / jumlahPenumpang, "KM")

print("\n==== JUMLAH PENUMPANG ====")
print("Jumlah Penumpang = ", jumlahPenumpang)

print("\n==== TOTAL PENDAPATAN KASIR ====")
print("Total Pendapatan = ", totalPendapatan)

print("\n==== JARAK TERJAUH PENUMPANG ====")
print("Jarak Terjauhnya = ", jarakTerjauh, "KM")