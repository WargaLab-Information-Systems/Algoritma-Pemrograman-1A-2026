def tampilkan_menu():
    print()
    print("Music Player - Playlist:")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")

def buat_playlist(playlist):
    nama = input("Nama playlist: ")
    if nama == "":
        print("Nama playlist tidak boleh kosong.")
    elif nama in playlist:
        print(f"Playlist '{nama}' sudah ada.")
    else:
        playlist[nama] = {}
        print(f"Playlist '{nama}' dibuat.")

def tambah_lagu(playlist):
    nama = input("Nama playlist: ")
    if nama not in playlist:
        print(f"Playlist '{nama}' tidak ditemukan.")
        return
    judul = input("Judul lagu: ")
    penyanyi = input("Penyanyi: ")
    if judul == "" or penyanyi == "":
        print("Judul dan penyanyi tidak boleh kosong.")
    else:
        playlist[nama][judul] = penyanyi
        print(f"Lagu '{judul}' ditambahkan ke '{nama}'.")

def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Belum ada playlist.")
        return
    for nama, lagu in playlist.items():
        print()
        print(f"Playlist: {nama}")
        if len(lagu) == 0:
            print("  (kosong)")
        else:
            nomor = 1
            for judul, penyanyi in lagu.items():
                print(f"  {nomor}. {judul} - {penyanyi}")
                nomor += 1

def cari_lagu(playlist):
    kata = input("Judul lagu yang dicari: ").lower()
    ditemukan = False
    for nama, lagu in playlist.items():
        for judul, penyanyi in lagu.items():
            if kata in judul.lower():
                print(f"Ditemukan: '{judul}' - {penyanyi} (playlist: {nama})")
                ditemukan = True
    if not ditemukan:
        print("Lagu tidak ditemukan.")

def hapus_lagu(playlist):
    nama = input("Nama playlist: ")
    if nama not in playlist:
        print(f"Playlist '{nama}' tidak ditemukan.")
        return
    judul = input("Judul lagu yang dihapus: ")
    if judul in playlist[nama]:
        del playlist[nama][judul]
        print(f"Lagu '{judul}' dihapus dari '{nama}'.")
    else:
        print(f"Lagu '{judul}' tidak ada di playlist '{nama}'.")

def hapus_playlist(playlist):
    nama = input("Nama playlist yang dihapus: ")
    if nama in playlist:
        del playlist[nama]
        print(f"Playlist '{nama}' dihapus.")
    else:
        print(f"Playlist '{nama}' tidak ditemukan.")

def main():
    playlist = {}
    while True:
        tampilkan_menu()
        while True:
            try:
                pilihan = int(input("Pilih menu (1-6): "))
                break
            except ValueError:
                print("Masukan tidak valid")
                continue

        if pilihan == "1":
            buat_playlist(playlist)
        elif pilihan == "2":
            tambah_lagu(playlist)
        elif pilihan == "3":
            tampilkan_playlist(playlist)
        elif pilihan == "4":
            cari_lagu(playlist)
        elif pilihan == "5":
            hapus_lagu(playlist)
        elif pilihan == "6":
            hapus_playlist(playlist)
        elif pilihan == "7":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
