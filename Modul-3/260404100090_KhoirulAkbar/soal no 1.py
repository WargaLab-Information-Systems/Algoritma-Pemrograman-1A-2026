jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = float(input("masukkan jarak tempuh( 0 untuk selesai )=  " ))

    if jarak == 0:
        break

    if jarak <0 :
        print("jarak tidak valid ! masukkan ulang")
        continue 
    
    if jarak <= 5 :
        Tharif = 3000
    elif jarak <= 15 :
        Tharif = 3000 + (jarak - 5)* 1000
    else :
        Tharif = 13000 + (jarak - 15)* 500

    jumlah_penumpang += 1

    if jumlah_penumpang >= 5 : 
        Tharif = Tharif * 50 / 100
        print("mendapatkan diskon 50%")

    total_pendapatan += Tharif
    total_jarak += jarak

    if jarak > jarak_terjauh :
        jarak_terjauh = jarak

    print ("tarif penumpang = RP", int(Tharif))

    if jumlah_penumpang >0 :
        rata_rata = total_jarak / jumlah_penumpang
    else :
        rata_rata = 0

print ("jumlah penumpang = " , jumlah_penumpang)
print ("total pendapatan = RP" , int(total_pendapatan))
print ("jarak terjauh = " , jarak_terjauh,"km")
print ("rata rata jarak = " , (rata_rata,),"km")