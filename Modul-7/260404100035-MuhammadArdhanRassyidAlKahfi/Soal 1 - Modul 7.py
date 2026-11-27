todo = {}

while True:
    print("\n MENU TO-DO LIST ")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Hitung status tugas")
    print("6. Keluar")

    pilihan = input("Pilih menu: ").strip()

    if pilihan == "":
        print("Pilihan tidak boleh kosong!")
    elif not pilihan.isdigit():
        print("Pilihan harus berupa angka!")
    elif pilihan == "1":
        tugas = input("Masukkan nama tugas: ").strip()

        if tugas == "":
            print("Nama tugas tidak boleh kosong!")
        elif tugas in todo:
            print("Tugas sudah tersedia!")
        else:
            todo[tugas] = "Belum selesai"
            print("Tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if not todo:
            print("Belum ada tugas!")
        else:
            print("\n===== DAFTAR TUGAS =====")
            for tugas, status in todo.items():
                print(f"{tugas} : {status}")

    elif pilihan == "3":
        tugas = input("Masukkan nama tugas: ").strip()

        if tugas == "":
            print("Nama tugas tidak boleh kosong!")
        elif tugas not in todo:
            print("Tugas tidak ditemukan!")
        else:
            todo[tugas] = "Selesai"
            print("Tugas berhasil ditandai selesai!")

    elif pilihan == "4":
        tugas = input("Masukkan nama tugas: ").strip()

        if tugas == "":
            print("Nama tugas tidak boleh kosong!")
        elif tugas not in todo:
            print("Tugas tidak ditemukan!")
        else:
            del todo[tugas]
            print("Tugas berhasil dihapus!")

    elif pilihan == "5":
        selesai = list(todo.values()).count("Selesai")
        belum = list(todo.values()).count("Belum selesai")

        print(f"Jumlah tugas selesai: {selesai}")
        print(f"Jumlah tugas belum selesai: {belum}")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak tersedia!")