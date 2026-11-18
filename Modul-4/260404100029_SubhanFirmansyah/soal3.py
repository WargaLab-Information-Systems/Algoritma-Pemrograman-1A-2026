jarak = 4                                          

while 1:
    teks = input("Masukkan n: ")
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
    if n == 0:
        print("n harus bilangan bulat positif (minimal 1), ulangi")
        continue
    break

print()

for baris in range(1, n + 1):                      

    kanan = ""                                      
    kiri = ""                                     

    for j in range(1, baris + 1):                  
        angka = j % 10                             

        urutan = 0
        for c in "0123456789":                     
            if urutan == angka:
                kiri = kiri + c                    
                kanan = c + kanan                  
            urutan += 1

    teks = kiri

    for s in range(n - baris):                     
        teks = teks + " "

    for s in range(jarak):                         
        teks = teks + " "

    for s in range(n - baris):                     
        teks = teks + " "

    teks = teks + kanan
    print(teks)