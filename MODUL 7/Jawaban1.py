tugas = {}

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Tampilkan tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Hitung tugas selesai dan belum")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum selesai"
        print("Tugas berhasil ditambahkan.")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            for nama in tugas:
                print(nama, "-", tugas[nama])

    elif pilihan == "3":
        nama = input("Nama tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas ditandai selesai.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Nama tugas yang ingin dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "5":
        selesai = 0
        belum_selesai = 0
        for nama in tugas:
            if tugas[nama] == "Selesai":
                selesai = selesai + 1
            else:
                belum_selesai = belum_selesai + 1
        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum_selesai)

    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")