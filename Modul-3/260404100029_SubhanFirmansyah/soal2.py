while 1:
    teks = input("Masukkan tinggi setengah menara (2-15): ")
    if teks == "":
        print("Input tidak boleh kosong, ulangi")
        continue

    angka_valid = True
    jumlah_angka = 0
    posisi = 0
    for huruf in teks:                         
        posisi += 1
        if posisi == 1 and huruf == "-":       
            pass
        elif huruf >= "0" and huruf <= "9":
            jumlah_angka += 1
        else:
            angka_valid = False

    if angka_valid == False or jumlah_angka == 0:
        print("Input harus berupa bilangan bulat, ulangi")
        continue

    n = int(teks)                              
    if n < 0:
        print("Input tidak boleh negatif, ulangi")
        continue
    if n < 2 or n > 15:
        print("Input harus antara 2 sampai 15, ulangi")
        continue
    break

print()

for baris in range(1, 2 * n):                  

    if baris <= n:                             
        k = baris
    else:                                      
        k = 2 * n - baris

    teks = ""

    for s in range(n - k):                     
        teks = teks + " "

    for p in range(1, 2 * k):                  
        if p <= k:                             
            j = p
        else:                                  
            j = 2 * k - p

        angka = j % 10                         

        urutan = 0
        for c in "0123456789":                 
            if urutan == angka:
                teks = teks + c
            urutan += 1

    print(teks)