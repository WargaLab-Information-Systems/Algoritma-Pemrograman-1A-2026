def palindrom(kata):
    terbalik = ""
    for huruf in kata:                           
        terbalik = huruf + terbalik                

    if kata == terbalik:
        return True
    else:
        return False

def baca_kata():
    while 1:
        kata = input("Masukkan kata: ")
        if kata == "":                             
            print("Input tidak boleh kosong, ulangi")
            continue

        hanya_huruf = True
        angka_saja = True
        jumlah_angka = 0
        minus_depan = False
        posisi = 0

        for huruf in kata:                       
            posisi += 1
            if posisi == 1 and huruf == "-":
                minus_depan = True
                hanya_huruf = False
            elif huruf >= "0" and huruf <= "9":
                jumlah_angka += 1
                hanya_huruf = False
            else:
                angka_saja = False
                if (huruf >= "a" and huruf <= "z") or (huruf >= "A" and huruf <= "Z"):
                    pass
                else:
                    hanya_huruf = False

        if minus_depan and jumlah_angka > 0 and angka_saja:    
            print("Input tidak boleh berupa angka negatif, ulangi")
            continue
        if hanya_huruf == False:                               
            print("Input harus berupa kata (huruf saja), ulangi")
            continue

        return kata                               

kata = baca_kata()
hasil = palindrom(kata)

print("Hasil fungsi:", hasil)

if hasil == True:
    print("Kata", kata, "adalah palindrom")
else:
    print("Kata", kata, "bukan palindrom")