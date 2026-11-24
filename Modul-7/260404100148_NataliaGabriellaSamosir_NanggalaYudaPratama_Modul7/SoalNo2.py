# Program Pengelola Playlist Musik
# Menggunakan Dictionary di dalam Dictionary

# Dictionary utama kosong
playlist = {}

while True:
    print("\n===== PENGELOLA PLAYLIST MUSIK =====")
    print("1. Membuat Playlist")
    print("2. Menambahkan Lagu ke Playlist")
    print("3. Menampilkan Semua Playlist")
    print("4. Mencari Lagu")
    print("5. Menghapus Lagu dari Playlist")
    print("6. Menghapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    # 1. Membuat playlist
    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            print("Playlist tersebut sudah ada!")
        else:
            playlist[nama_playlist] = {}
            print("Playlist berhasil dibuat!")

    # 2. Menambahkan lagu ke playlist
    elif pilihan == "2":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul_lagu = input("Masukkan judul lagu: ")
            nama_penyanyi = input("Masukkan nama penyanyi: ")

            if judul_lagu in playlist[nama_playlist]:
                print("Lagu tersebut sudah ada di playlist!")
            else:
                playlist[nama_playlist][judul_lagu] = nama_penyanyi
                print("Lagu berhasil ditambahkan!")
        else:
            print("Playlist tidak ditemukan!")

    # 3. Menampilkan semua playlist
    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            print("\n===== DAFTAR PLAYLIST =====")

            for nama_playlist, daftar_lagu in playlist.items():
                print(f"\nPlaylist: {nama_playlist}")

                if len(daftar_lagu) == 0:
                    print("  Playlist masih kosong.")
                else:
                    for judul_lagu, nama_penyanyi in daftar_lagu.items():
                        print(f"  - {judul_lagu} | Penyanyi: {nama_penyanyi}")

    # 4. Mencari lagu
    elif pilihan == "4":
        judul_lagu = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False

        for nama_playlist, daftar_lagu in playlist.items():
            if judul_lagu in daftar_lagu:
                print(f"Lagu ditemukan!")
                print(f"Playlist  : {nama_playlist}")
                print(f"Judul    : {judul_lagu}")
                print(f"Penyanyi : {daftar_lagu[judul_lagu]}")
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan!")

    # 5. Menghapus lagu dari playlist
    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul_lagu = input("Masukkan judul lagu yang ingin dihapus: ")

            if judul_lagu in playlist[nama_playlist]:
                del playlist[nama_playlist][judul_lagu]
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan dalam playlist tersebut!")
        else:
            print("Playlist tidak ditemukan!")

    # 6. Menghapus playlist
    elif pilihan == "6":
        nama_playlist = input("Masukkan nama playlist yang ingin dihapus: ")

        if nama_playlist in playlist:
            del playlist[nama_playlist]
            print("Playlist berhasil dihapus!")
        else:
            print("Playlist tidak ditemukan!")

    # 7. Keluar
    elif pilihan == "7":
        print("Program pengelola playlist selesai.")
        break

    # Pilihan menu tidak valid
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-7.")