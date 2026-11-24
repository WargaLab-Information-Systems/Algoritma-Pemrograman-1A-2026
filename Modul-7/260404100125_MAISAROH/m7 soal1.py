daftar_tugas = {}

while True:
    print("\n===== MENU TO-DO LIST =====")
    print("1. tambah tugas")
    print("2. tampilkan semua tugas")
    print("3. tandai tugas selesai")
    print("4. hapus tugas")
    print("5. jumlah tugas selesai dan belum")
    print("6. keluar")

    pilihan = input("pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("masukkan nama tugas: ")
        daftar_tugas[nama] = "belum selesai"
        print("tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if len(daftar_tugas) == 0:
            print("belum ada tugas.")
        else:
            print("\ndaftar tugas:")
            for nama, status in daftar_tugas.items():
                print(nama, ":", status)

    elif pilihan == "3":
        nama = input("masukkan nama tugas yang selesai: ")

        if nama in daftar_tugas:
            daftar_tugas[nama] = "selesai"
            print("tugas berhasil ditandai selesai!")
        else:
            print("tugas tidak ditemukan.")

    elif pilihan == "4":
        nama = input("masukkan nama tugas yang ingin dihapus: ")

        if nama in daftar_tugas:
            del daftar_tugas[nama]
            print("tugas berhasil dihapus!")
        else:
            print("tugas tidak ditemukan.")
    elif pilihan == "5":
        selesai = 0
        belum = 0

        for status in daftar_tugas.values():
            if status == "selesai":
                selesai += 1
            else:
                belum += 1

        print("jumlah tugas selesai:", selesai)
        print("jumlah tugas belum selesai:", belum)

    elif pilihan == "6":
        print("program selesai. terima kasih!")
        break

    else:
        print("pilihan tidak valid!")
