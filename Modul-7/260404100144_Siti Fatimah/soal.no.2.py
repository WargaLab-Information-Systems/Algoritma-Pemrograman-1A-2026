
# Membuat dictionary kosong
playlist = {}

while True:
    print("=== MENU PLAYLIST MUSIK ===")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    # Membuat playlist
    if pilihan == "1":
        nama = input("Masukkan nama playlist: ")

        if nama not in playlist:
            playlist[nama] = {}
            print("Playlist berhasil dibuat!")
        else:
            print("Playlist sudah tersedia.")

    # Menambahkan lagu
    elif pilihan == "2":
        nama = input("Masukkan nama playlist: ")

        try:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan!")

        except KeyError:
            print("Playlist tidak ditemukan.")

    # Menampilkan semua playlist
    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)

                if len(lagu) == 0:
                    print("Belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print(judul, "-", penyanyi)

    # Mencari lagu
    elif pilihan == "4":
        judul = input("Masukkan judul lagu: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            try:
                penyanyi = lagu[judul]
                print("Lagu ditemukan!")
                print("Playlist:", nama)
                print("Penyanyi:", penyanyi)
                ditemukan = True
            except KeyError:
                pass

        if ditemukan == False:
            print("Lagu tidak ditemukan.")

    # Menghapus lagu
    elif pilihan == "5":
        nama = input("Masukkan nama playlist: ")

        try:
            judul = input("Masukkan judul lagu: ")
            del playlist[nama][judul]
            print("Lagu berhasil dihapus!")

        except KeyError:
            print("Playlist atau lagu tidak ditemukan.")

    # Menghapus playlist
    elif pilihan == "6":
        nama = input("Masukkan nama playlist: ")

        try:
            del playlist[nama]
            print("Playlist berhasil dihapus!")

        except KeyError:
            print("Playlist tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
