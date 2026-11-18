playlist = {
    "nama playlist": {"judul lagu": "penyanyi"}
}
def baca_menu():
    while 1:
        teks = input("Pilih menu (0-6): ")
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
        if pilihan > 6:
            print("Pilihan hanya 0 sampai 6, ulangi")
            continue

        return pilihan

def baca_teks(pesan, jenis):
    while 1:
        teks = input(pesan)
        if teks == "":                             
            print("Input tidak boleh kosong, ulangi")
            continue

        ada_isi = False                            
        for huruf in teks:
            if huruf != " ":
                ada_isi = True
        if ada_isi == False:
            print("Input tidak boleh kosong, ulangi")
            continue

        angka_sah = False
        try:
            angka = float(teks)                    
            if angka - angka == 0:                 
                angka_sah = True
        except ValueError:
            angka_sah = False                      

        if angka_sah:
            if angka < 0:                          
                print("Input tidak boleh berupa angka negatif, ulangi")
            else:                                  
                print(jenis, "harus berupa teks, bukan angka, ulangi")
            continue

        return teks

playlist = {}                                      

while 1:
    print()
    print("===== MENU PLAYLIST MUSIK =====")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("0. Keluar")

    pilihan = baca_menu()

    if pilihan == 0:
        print("Program selesai")
        break

    elif pilihan == 1:
        nama_pl = baca_teks("Nama playlist baru: ", "Nama playlist")
        if nama_pl in playlist:
            print("Playlist", nama_pl, "sudah ada")
        else:
            playlist[nama_pl] = {}                 
            print("Playlist", nama_pl, "dibuat")

    elif pilihan == 2:                             
        if len(playlist) == 0:
            print("Belum ada playlist, buat playlist dulu")
        else:
            nama_pl = baca_teks("Nama playlist tujuan: ", "Nama playlist")

            ditemukan = True
            try:
                isi = playlist[nama_pl]            
            except KeyError:
                ditemukan = False

            if ditemukan == False:
                print("Playlist", nama_pl, "tidak ditemukan")
            else:
                judul = baca_teks("Judul lagu: ", "Judul lagu")
                penyanyi = baca_teks("Penyanyi: ", "Nama penyanyi")
                if judul in isi:
                    print("Lagu", judul, "sudah ada di playlist", nama_pl)
                else:
                    isi[judul] = penyanyi          
                    print("Lagu", judul, "ditambahkan ke", nama_pl)

    elif pilihan == 3:                             
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            for nama_pl in playlist:
                print()
                print("Playlist:", nama_pl, "(", len(playlist[nama_pl]), "lagu )")
                if len(playlist[nama_pl]) == 0:
                    print("   (kosong)")
                else:
                    for judul in playlist[nama_pl]:
                        print("   -", judul, "oleh", playlist[nama_pl][judul])

    elif pilihan == 4:                             
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            judul = baca_teks("Judul lagu yang dicari: ", "Judul lagu")
            jumlah_ketemu = 0
            for nama_pl in playlist:
                if judul in playlist[nama_pl]:
                    print(judul, "oleh", playlist[nama_pl][judul], "ada di playlist", nama_pl)
                    jumlah_ketemu += 1
            if jumlah_ketemu == 0:
                print("Lagu", judul, "tidak ditemukan di playlist mana pun")

    elif pilihan == 5:                             
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            nama_pl = baca_teks("Nama playlist: ", "Nama playlist")

            ditemukan = True
            try:
                isi = playlist[nama_pl]            
            except KeyError:
                ditemukan = False

            if ditemukan == False:
                print("Playlist", nama_pl, "tidak ditemukan")
            else:
                judul = baca_teks("Judul lagu yang dihapus: ", "Judul lagu")
                try:
                    del isi[judul]                 
                    print("Lagu", judul, "dihapus dari", nama_pl)
                except KeyError:
                    print("Lagu", judul, "tidak ditemukan di playlist", nama_pl)
    else:                                          
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            nama_pl = baca_teks("Nama playlist yang dihapus: ", "Nama playlist")
            try:
                del playlist[nama_pl]              
                print("Playlist", nama_pl, "dihapus")
            except KeyError:
                print("Playlist", nama_pl, "tidak ditemukan")