jumlahBeasiswa = 0
for u in range(1,6) :
    print ("mahasiswa ke : " , u)
    nama = input("masukkan nama : ")
    ipk  = float(input("mahasiswa IPK : "))
    penghasilan = int(input("penghasilan perbulan : "))

    if ipk >= 3.00 :       
    
        if penghasilan <= 3000000  :
            print(" 'mendapaatkan beasiswa penuh' ")
            jumlahBeasiswa += 1
        
        elif penghasilan <= 5000000 :
            print (" 'mendapatkan beasiswa sebagian' ")
        else : 
            print (" 'mahasiswa tidak mendapatkan beasiswa' ")
    else :
        print (" 'tidak memenuhi syarat' ")
        
    print ("jumlah beasiswa : ", jumlahBeasiswa)
    if jumlahBeasiswa == 3 :
        print(" 'kuota beasiswa terpenuhi' ")
        break