playlist = {}

while True:
    print("\n MENU PLAYLIST MUSIK ")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu: ").strip()

    if pilihan == "":
        print("Pilihan tidak boleh kosong!")
    elif not pilihan.isdigit():
        print("Pilihan harus berupa angka!")

    elif pilihan == "1":
        nama = input("Masukkan nama playlist: ").strip()

        if nama == "":
            print("Nama playlist tidak boleh kosong!")
        elif nama in playlist:
            print("Playlist sudah tersedia!")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat!")

    elif pilihan == "2":
        nama = input("Masukkan nama playlist: ").strip()

        if nama == "":
            print("Nama playlist tidak boleh kosong!")
        elif nama not in playlist:
            print("Playlist tidak ditemukan!")
        else:
            judul = input("Masukkan judul lagu: ").strip()
            penyanyi = input("Masukkan nama penyanyi: ").strip()

            if judul == "" or penyanyi == "":
                print("Judul lagu dan penyanyi tidak boleh kosong!")
            elif judul in playlist[nama]:
                print("Lagu sudah tersedia di playlist!")
            else:
                playlist[nama][judul] = penyanyi
                print("Lagu berhasil ditambahkan!")

    elif pilihan == "3":
        if not playlist:
            print("Belum ada playlist!")
        else:
            for nama, lagu in playlist.items():
                print(f"\nPlaylist: {nama}")

                if not lagu:
                    print("Belum ada lagu!")
                else:
                    for judul, penyanyi in lagu.items():
                        print(f"{judul} - {penyanyi}")

    elif pilihan == "4":
        judul = input("Masukkan judul lagu: ").strip()

        if judul == "":
            print("Judul lagu tidak boleh kosong!")
        else:
            ditemukan = False

            for nama, lagu in playlist.items():
                if judul in lagu:
                    print(f"Lagu: {judul}")
                    print(f"Penyanyi: {lagu[judul]}")
                    print(f"Playlist: {nama}")
                    ditemukan = True

            if not ditemukan:
                print("Lagu tidak ditemukan!")

    elif pilihan == "5":
        nama = input("Masukkan nama playlist: ").strip()

        if nama == "":
            print("Nama playlist tidak boleh kosong!")
        elif nama not in playlist:
            print("Playlist tidak ditemukan!")
        else:
            judul = input("Masukkan judul lagu: ").strip()

            if judul == "":
                print("Judul lagu tidak boleh kosong!")
            elif judul not in playlist[nama]:
                print("Lagu tidak ditemukan!")
            else:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus!")

    elif pilihan == "6":
        nama = input("Masukkan nama playlist: ").strip()

        if nama == "":
            print("Nama playlist tidak boleh kosong!")
        elif nama not in playlist:
            print("Playlist tidak ditemukan!")
        else:
            del playlist[nama]
            print("Playlist berhasil dihapus!")

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak tersedia!")