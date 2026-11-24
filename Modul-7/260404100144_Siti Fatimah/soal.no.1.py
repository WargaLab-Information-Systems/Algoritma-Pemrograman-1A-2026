
# Membuat dictionary kosong
tugas = {}

while True:
    print("=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    # Menambah tugas
    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")
        tugas[nama] = "Belum selesai"
        print("Tugas berhasil ditambahkan!")

    # Menampilkan tugas
    elif pilihan == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            print("Daftar Tugas:")
            for nama, status in tugas.items():
                print(nama, ":", status)

    # Menandai tugas selesai
    elif pilihan == "3":
        nama = input("Masukkan nama tugas: ")

        try:
            tugas[nama] = "Selesai"
            print("Tugas berhasil diselesaikan!")
        except KeyError:
            print("Tugas tidak ditemukan.")

    # Menghapus tugas
    elif pilihan == "4":
        nama = input("Masukkan nama tugas: ")

        try:
            del tugas[nama]
            print("Tugas berhasil dihapus!")
        except KeyError:
            print("Tugas tidak ditemukan.")

    # Menghitung jumlah tugas
    elif pilihan == "5":
        selesai = list(tugas.values()).count("Selesai")
        belum = list(tugas.values()).count("Belum selesai")

        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
