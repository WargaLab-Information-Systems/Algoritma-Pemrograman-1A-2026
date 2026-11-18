def baca_jumlah(pesan):
    while 1:
        teks = input(pesan)
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
            print("Jumlah PC minimal 1, ulangi")
            continue

        return n

def baca_nama_pc(pesan):
    while 1:
        nama = input(pesan)
        if nama == "":                             
            print("Input tidak boleh kosong, ulangi")
            continue

        karakter_salah = False
        ada_isi = False                            
        angka_saja = True                          
        jumlah_angka = 0
        minus_depan = False
        posisi = 0

        for huruf in nama:                         
            posisi += 1
            if posisi == 1 and huruf == "-":
                minus_depan = True
            elif huruf >= "0" and huruf <= "9":
                jumlah_angka += 1
                ada_isi = True
            elif (huruf >= "a" and huruf <= "z") or (huruf >= "A" and huruf <= "Z"):
                ada_isi = True
                angka_saja = False
            elif huruf == "-" or huruf == "_" or huruf == " ":
                angka_saja = False
            else:
                karakter_salah = True
                angka_saja = False

        if minus_depan and jumlah_angka > 0 and angka_saja:    
            print("Nama tidak boleh berupa angka negatif, ulangi")
            continue
        if karakter_salah:                                    
            print("Nama hanya boleh berisi huruf, angka, spasi, - dan _, ulangi")
            continue
        if ada_isi == False:
            print("Nama harus memuat huruf atau angka, ulangi")
            continue

        return nama

def baca_status(pesan):
    while 1:
        status = input(pesan)
        if status == "":                          
            print("Input tidak boleh kosong, ulangi")
            continue

        hanya_huruf = True
        angka_saja = True
        jumlah_angka = 0
        minus_depan = False
        posisi = 0

        for huruf in status:                       
            posisi += 1
            if posisi == 1 and huruf == "-":
                minus_depan = True
                hanya_huruf = False
            elif huruf >= "0" and huruf <= "9":
                jumlah_angka += 1
                hanya_huruf = False
            elif (huruf >= "a" and huruf <= "z") or (huruf >= "A" and huruf <= "Z"):
                angka_saja = False
            else:
                angka_saja = False
                hanya_huruf = False

        if minus_depan and jumlah_angka > 0 and angka_saja:    
            print("Status tidak boleh berupa angka negatif, ulangi")
            continue
        if hanya_huruf == False:
            print("Status harus berupa huruf saja, ulangi")
            continue

        if status == "Normal" or status == "normal":
            return "Normal"
        if status == "Rusak" or status == "rusak":
            return "Rusak"
        print("Status hanya boleh Normal atau Rusak, ulangi")

def evaluasi(pc):
    ram = int(pc[2])                               
    if pc[1] == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

inventaris = []                                    

jumlah_pc = baca_jumlah("Jumlah PC yang akan didata: ")

for i in range(1, jumlah_pc + 1):
    print("--- PC ke-", i, "---")
    nama = baca_nama_pc("Nama PC: ")
    status = baca_status("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")            
    inventaris.append([nama, status, ram])         

print()
print("=== HASIL EVALUASI ===")

for pc in inventaris:
    try:
        kelayakan = evaluasi(pc)
    except ValueError:                             
        kelayakan = "Format RAM Kacau"

    
    hasil = '{ "PC": "' + pc[0] + '", "Status": "' + kelayakan + '" }'
    print(hasil)