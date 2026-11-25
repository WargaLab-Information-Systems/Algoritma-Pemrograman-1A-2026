playlist = {}

while True:
    print(" MENU PLAYLIST MUSIK ")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Semua Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Jumlah Lagu Setiap Playlist")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ")

    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist: ")
        if nama_playlist in playlist:
            print("Playlist sudah tersedia.")
        else:
            playlist[nama_playlist] = {}
            print("Playlist berhasil dibuat.")

    elif pilihan == "2":
        nama_playlist = input("Masukkan nama playlist: ")
        if nama_playlist in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama_playlist][judul] = penyanyi
            print("Lagu berhasil ditambahkan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama_playlist, lagu in playlist.items():
                print("\nPlaylist:", nama_playlist)
                if len(lagu) == 0:
                    print("Belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print("-", judul, ":", penyanyi)

    elif pilihan == "4":
        cari = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False
        for nama_playlist, lagu in playlist.items():
            for judul, penyanyi in lagu.items():
                if cari == judul:
                    print("Lagu ditemukan!")
                    print("Playlist:", nama_playlist)
                    print("Judul Lagu:", judul)
                    print("Penyanyi:", penyanyi)
                    ditemukan = True
        if ditemukan == False:
            print("Lagu tidak ditemukan.")

    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")
        judul = input("Masukkan judul lagu yang ingin dihapus: ")

        try:
            del playlist[nama_playlist][judul]
            print("Lagu berhasil dihapus.")
        except KeyError:
            print("Playlist atau lagu tidak ditemukan.")

    elif pilihan == "6":
        nama_playlist = input("Masukkan nama playlist: ")

        try:
            del playlist[nama_playlist]
            print("Playlist berhasil dihapus.")
        except KeyError:
            print("Playlist tidak ditemukan.")

    elif pilihan == "7":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            print("Jumlah Lagu Setiap Playlist:")
            for nama_playlist, lagu in playlist.items():
                print(nama_playlist, ":", len(lagu), "lagu")

    elif pilihan == "8":
        print("Program Playlist selesai.")
        break
    else:
        print("Pilihan tidak valid!")
