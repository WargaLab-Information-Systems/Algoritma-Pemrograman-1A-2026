tugas = {}
while True:
    print(" MENU TO-DO LIST ")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Hitung Status Tugas")
    print("6. Cari Tugas")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")
        if nama in tugas:
            print("Tugas sudah ada!")
        else:
            tugas[nama] = "Belum Selesai"
            print("Tugas berhasil ditambahkan.")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for nama, status in tugas.items():
                print(nama, ":", status)

    elif pilihan == "3":
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil ditandai selesai.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Masukkan nama tugas: ")

        try:
            del tugas[nama]
            print("Tugas berhasil dihapus.")
        except KeyError:
            print("Tugas tidak ditemukan.")

    elif pilihan == "5":
        selesai = 0
        belum = 0
        for status in tugas.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1

        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum)

    elif pilihan == "6":
        nama = input("Masukkan nama tugas yang dicari: ")
        if nama in tugas:
            print("Tugas ditemukan!")
            print("Nama Tugas:", nama)
            print("Status:", tugas[nama])
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
