# Fungsi validasi input teks
def validasi_teks(pesan):
    while True:
        masukan = input(pesan)
        if not masukan:
            print("Masukan tidak boleh kosong!")
            continue
        if masukan[0] == "-":
            print("Masukan tidak boleh minus!")
            continue

        tidak_valid = False
        for c in masukan:
            if not ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == ' '):
                tidak_valid = True
                break

        if tidak_valid:
            print("Masukan hanya boleh huruf atau spasi!")
            continue
        return masukan

# Fungsi validasi pilihan menu (1-7)
def validasi_angka(pesan):
    while True:
        angka = input(pesan)
        if not angka:
            print("Masukan tidak boleh kosong!")
            continue
        if angka[0] == "-":
            print("Masukan tidak boleh minus!")
            continue

        tidak_valid = False
        for c in angka:
            if not (c >= '0' and c <= '9'):
                tidak_valid = True
                break

        if tidak_valid:
            print("Masukan hanya boleh angka!")
            continue
        if int(angka) < 1 or int(angka) > 7:
            print("Pilihan menu hanya 1-7!")
            continue
        return angka

# Program Playlist Musik
playlists = {}

while True:
    print()
    print("<===== MENU PLAYLIST MUSIK =====>")
    print("1. Buat Playlist Baru")
    print("2. Tambah Lagu ke Playlist")
    print("3. Tampilkan Semua Playlist & Lagu")
    print("4. Cari Lagu")
    print("5. Hapus Lagu dari Playlist")
    print("6. Hapus Playlist")
    print("7. Keluar")
    print()

    pilihan = validasi_angka("Pilih menu (1-7): ")

    if pilihan == "1":
        print()
        print("Ketik 'selesai' untuk keluar dari menu pembuatan playlist.")
        while True:
            nama_pl = validasi_teks("Masukkan nama playlist baru: ")
            if nama_pl.lower() == "selesai":
                print("Kembali ke menu utama.")
                break
            if nama_pl in playlists:
                print("Playlist '" + nama_pl + "' sudah ada.")
            else:
                playlists[nama_pl] = {}
                print("Playlist '" + nama_pl + "' berhasil dibuat.")

    elif pilihan == "2":
        print()
        print("Ketik 'selesai' untuk keluar dari menu tambah lagu.")
        while True:
            nama_pl = validasi_teks("Masukkan nama playlist tujuan: ")
            if nama_pl.lower() == "selesai":
                print("Kembali ke menu utama.")
                break
            try:
                isi_pl = playlists[nama_pl]
                while True:
                    judul = validasi_teks("Masukkan judul lagu (atau 'selesai'): ")
                    if judul.lower() == "selesai":
                        break
                    penyanyi = validasi_teks("Masukkan nama penyanyi: ")
                    isi_pl[judul] = penyanyi
                    print("Lagu '" + judul + "' berhasil ditambahkan ke '" + nama_pl + "'.")
            except KeyError:
                print("Error ditangani: Playlist '" + nama_pl + "' tidak ditemukan!")

    elif pilihan == "3":
        print()
        if len(playlists) == 0:
            print("Belum ada playlist yang tersimpan.")
        else:
            print("--- DAFTAR PLAYLIST & LAGU ---")
            for nama_pl in playlists:
                print("\nPlaylist : " + nama_pl)
                if len(playlists[nama_pl]) == 0:
                    print("  (Playlist masih kosong)")
                else:
                    for judul in playlists[nama_pl]:
                        penyanyi = playlists[nama_pl][judul]
                        print("  - " + judul.ljust(22) + " | Penyanyi : " + penyanyi)

    elif pilihan == "4":
        print()
        print("Ketik 'selesai' untuk keluar dari menu pencarian lagu.")
        while True:
            cari = validasi_teks("Masukkan judul lagu yang dicari: ")
            if cari.lower() == "selesai":
                print("Kembali ke menu utama.")
                break
            ditemukan = False
            for nama_pl in playlists:
                try:
                    penyanyi = playlists[nama_pl][cari]
                    print("Ditemukan di playlist '" + nama_pl + "' -> " + cari + " (" + penyanyi + ")")
                    ditemukan = True
                except KeyError:
                    pass
            if not ditemukan:
                print("Lagu '" + cari + "' tidak ditemukan di playlist mana pun.")

    elif pilihan == "5":
        print()
        print("Ketik 'selesai' untuk keluar dari menu hapus lagu.")
        while True:
            nama_pl = validasi_teks("Masukkan nama playlist: ")
            if nama_pl.lower() == "selesai":
                print("Kembali ke menu utama.")
                break
            judul = validasi_teks("Masukkan judul lagu yang dihapus: ")
            if judul.lower() == "selesai":
                print("Kembali ke menu utama.")
                break
            try:
                del playlists[nama_pl][judul]
                print("Lagu '" + judul + "' berhasil dihapus dari '" + nama_pl + "'.")
            except KeyError:
                print("Error ditangani: Playlist atau lagu yang dituju tidak ditemukan!")

    elif pilihan == "6":
        print()
        print("Ketik 'selesai' untuk keluar dari menu hapus playlist.")
        while True:
            nama_pl = validasi_teks("Masukkan nama playlist yang dihapus: ")
            if nama_pl.lower() == "selesai":
                print("Kembali ke menu utama.")
                break
            try:
                del playlists[nama_pl]
                print("Playlist '" + nama_pl + "' berhasil dihapus.")
            except KeyError:
                print("Error ditangani: Playlist '" + nama_pl + "' tidak ditemukan!")

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak valid!")