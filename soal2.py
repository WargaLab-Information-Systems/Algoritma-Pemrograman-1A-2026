playlist = {}

def input_menu():
    while True:
        pilihan = input("Pilih menu: ").strip()
        if not pilihan:
            print("Input tidak boleh kosong")
            continue
        try:
            pilihan = int(pilihan)
        except ValueError:
            print("Masukkan angka untuk memilih menu")
            continue
        if pilihan < 0:
            print("Angka tidak boleh negatif")
            continue
        return pilihan


def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks:
            return teks
        print("Input tidak boleh kosong")


while True:
    print()
    print("MENU PLAYLIST MUSIK")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("0. Keluar")
    pilih = input_menu()

    if pilih == 1:
        nama = input_teks("Nama playlist: ")
        if nama in playlist:
            print("Playlist itu sudah ada")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat")

    elif pilih == 2:
        nama = input_teks("Masukkan ke playlist: ")
        try:
            isi = playlist[nama]
            judul = input_teks("Judul lagu: ")
            penyanyi = input_teks("Penyanyi: ")
            if judul in isi:
                print("Lagu itu sudah ada di playlist")
            else:
                isi[judul] = penyanyi
                print("Lagu berhasil ditambah")
        except KeyError:
            print("Playlist tidak ditemukan")

    elif pilih == 3:
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            for nama in playlist:
                print()
                print("Playlist:", nama)
                if len(playlist[nama]) == 0:
                    print("   (kosong)")
                else:
                    for judul in playlist[nama]:
                        print("   -", judul, "oleh", playlist[nama][judul])

    elif pilih == 4:
        cari = input_teks("Judul lagu yang dicari: ")
        ketemu = False
        for nama in playlist:
            if cari in playlist[nama]:
                print("Ketemu di playlist", nama, "- penyanyi:", playlist[nama][cari])
                ketemu = True
        if ketemu == False:
            print("Lagu tidak ditemukan")

    elif pilih == 5:
        nama = input_teks("Dari playlist: ")
        try:
            isi = playlist[nama]
            judul = input_teks("Judul lagu yang dihapus: ")
            try:
                del isi[judul]
                print("Lagu dihapus")
            except KeyError:
                print("Lagu tidak ditemukan di playlist itu")
        except KeyError:
            print("Playlist tidak ditemukan")

    elif pilih == 6:
        nama = input_teks("Playlist yang mau dihapus: ")
        try:
            del playlist[nama]
            print("Playlist dihapus")
        except KeyError:
            print("Playlist tidak ditemukan")

    elif pilih == 0:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak ada")