def baca_menu():
    while 1:
        teks = input("Pilih menu (0-5): ")
        if teks == "":                             
            print("Input tidak boleh kosong, ulangi")
            continue

        try:
            pilihan = int(teks)                
        except ValueError:
            print("Input harus berupa angka bulat, ulangi")
            continue

        if pilihan < 0:                            
            print("Pilihan tidak boleh negatif, ulangi")
            continue
        if pilihan > 5:
            print("Pilihan hanya 0 sampai 5, ulangi")
            continue

        return pilihan

def baca_tugas(pesan):
    while 1:
        nama = input(pesan)
        if nama == "":                             
            print("Input tidak boleh kosong, ulangi")
            continue

        ada_isi = False                            
        for huruf in nama:
            if huruf != " ":
                ada_isi = True
        if ada_isi == False:
            print("Input tidak boleh kosong, ulangi")
            continue

        angka_sah = False
        try:
            angka = float(nama)                    
            if angka - angka == 0:                 
                angka_sah = True
        except ValueError:
            angka_sah = False                      

        if angka_sah:
            if angka < 0:                          
                print("Input tidak boleh berupa angka negatif, ulangi")
            else:                                  
                print("Nama tugas harus berupa teks, bukan angka, ulangi")
            continue
        return nama

tugas = {}                                         

while 1:
    print()
    print("===== MENU TO-DO LIST =====")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum")
    print("0. Keluar")

    pilihan = baca_menu()

    if pilihan == 0:
        print("Program selesai")
        break

    elif pilihan == 1:                             
        nama = baca_tugas("Nama tugas baru: ")
        if nama in tugas:                          
            print("Tugas", nama, "sudah ada")
        else:
            tugas[nama] = "Belum selesai"          
            print("Tugas", nama, "ditambahkan")

    elif pilihan == 2:                             
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            print("--- Daftar tugas ---")
            for nama in tugas:
                print("-", nama, ":", tugas[nama])

    elif pilihan == 3:                             
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            nama = baca_tugas("Nama tugas yang selesai: ")
            try:
                if tugas[nama] == "Selesai":       
                    print("Tugas", nama, "sudah berstatus selesai")
                else:
                    tugas[nama] = "Selesai"        
                    print("Tugas", nama, "ditandai selesai")
            except KeyError:
                print("Tugas", nama, "tidak ditemukan")

    elif pilihan == 4:                             
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            nama = baca_tugas("Nama tugas yang dihapus: ")
            try:
                del tugas[nama]                    
                print("Tugas", nama, "dihapus")
            except KeyError:
                print("Tugas", nama, "tidak ditemukan")
    else:                                          
        selesai = 0
        belum = 0
        for nama in tugas:
            if tugas[nama] == "Selesai":
                selesai += 1
            else:
                belum += 1
        print("Tugas selesai :", selesai)
        print("Tugas belum   :", belum)
        print("Total tugas   :", len(tugas))