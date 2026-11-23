jumlahBaris = int(input("Masukkan jumlah baris: "))  

for nomorBaris in range(1, jumlahBaris + 1):                
    for angka in range(1, nomorBaris + 1):            
        print(angka, end=" ")                
    for s in range(2 * (jumlahBaris - nomorBaris) + 1):     
        print(" ", end=" ")
    for angka in range(nomorBaris, 0, -1):            
        print(angka, end=" ")
    print()