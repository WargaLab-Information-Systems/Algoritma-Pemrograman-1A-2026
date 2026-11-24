playlist = {}

while True:
    print("\n===== MENU PLAYLIST MUSIK =====")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Semua Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            print("Playlist sudah ada!")
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
                        print(judul, "-", penyanyi)

    elif pilihan == "4":
        cari = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False

        for nama_playlist, lagu in playlist.items():
            if cari in lagu:
                print("Lagu ditemukan!")
                print("Playlist:", nama_playlist)
                print("Judul:", cari)
                print("Penyanyi:", lagu[cari])
                ditemukan = True

        if ditemukan == False:
            print("Lagu tidak ditemukan.")

    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul = input("Masukkan judul lagu yang ingin dihapus: ")

            if judul in playlist[nama_playlist]:
                del playlist[nama_playlist][judul]
                print("Lagu berhasil dihapus.")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "6":
        nama_playlist = input("Masukkan nama playlist yang ingin dihapus: ")

        if nama_playlist in playlist:
            del playlist[nama_playlist]
            print("Playlist berhasil dihapus.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
