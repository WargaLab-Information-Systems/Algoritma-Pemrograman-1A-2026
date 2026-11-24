playlist = {}

while True:
    print("\n===== MENU PLAYLIST MUSIK =====")
    print("1. buat playlist")
    print("2. tambah lagu")
    print("3. tampilkan semua playlist")
    print("4. cari lagu")
    print("5. hapus lagu")
    print("6. hapus playlist")
    print("7. keluar")

    pilihan = input("pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("masukkan nama playlist: ")

        if nama not in playlist:
            playlist[nama] = {}
            print("playlist berhasil dibuat!")
        else:
            print("playlist sudah tersedia.")

    elif pilihan == "2":
        nama = input("masukkan nama playlist: ")

        if nama in playlist:
            judul = input("masukkan judul lagu: ")
            penyanyi = input("masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi
            print("lagu berhasil ditambahkan!")
        else:
            print("playlist tidak ditemukan.")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print("\nplaylist:", nama)

                if len(lagu) == 0:
                    print("belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print(judul, "-", penyanyi)

    elif pilihan == "4":
        judul = input("masukkan judul lagu yang dicari: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            if judul in lagu:
                print("lagu ditemukan!")
                print("Playlist:", nama)
                print("penyanyi:", lagu[judul])
                ditemukan = True

        if not ditemukan:
            print("lagu tidak ditemukan.")

    elif pilihan == "5":
        nama = input("masukkan nama playlist: ")

        if nama in playlist:
            judul = input("masukkan judul lagu yang ingin dihapus: ")

            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("lagu berhasil dihapus!")
            else:
                print("lagu tidak ditemukan.")
        else:
            print("playlist tidak ditemukan.")

    elif pilihan == "6":
        nama = input("masukkan nama playlist yang ingin dihapus: ")

        if nama in playlist:
            del playlist[nama]
            print("playlist berhasil dihapus!")
        else:
            print("playlist tidak ditemukan.")

    elif pilihan == "7":
        print("program selesai. terima kasih!")
        break

    else:
        print("pilihan tidak valid!")
