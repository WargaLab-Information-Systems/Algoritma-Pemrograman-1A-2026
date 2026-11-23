# Program To-Do List menggunakan Dictionary

# Dictionary kosong
todo_list = {}

while True:
    print("\n===== MENU TO-DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Tampilkan Jumlah Tugas")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    # 1. Menambahkan tugas
    if pilihan == "1":
        nama_tugas = input("Masukkan nama tugas: ")

        if nama_tugas in todo_list:
            print("Tugas tersebut sudah ada!")
        else:
            todo_list[nama_tugas] = "Belum Selesai"
            print("Tugas berhasil ditambahkan!")

    # 2. Menampilkan semua tugas
    elif pilihan == "2":
        if len(todo_list) == 0:
            print("Belum ada tugas.")
        else:
            print("\n===== DAFTAR TUGAS =====")
            for nama, status in todo_list.items():
                print(f"- {nama} : {status}")

    # 3. Menandai tugas selesai
    elif pilihan == "3":
        nama_tugas = input("Masukkan nama tugas yang selesai: ")

        if nama_tugas in todo_list:
            todo_list[nama_tugas] = "Selesai"
            print("Tugas berhasil ditandai selesai!")
        else:
            print("Tugas tidak ditemukan!")

    # 4. Menghapus tugas
    elif pilihan == "4":
        nama_tugas = input("Masukkan nama tugas yang ingin dihapus: ")

        if nama_tugas in todo_list:
            del todo_list[nama_tugas]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan!")

    # 5. Menampilkan jumlah tugas selesai dan belum selesai
    elif pilihan == "5":
        selesai = 0
        belum_selesai = 0

        for status in todo_list.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum_selesai += 1

        print("\n===== JUMLAH TUGAS =====")
        print(f"Tugas selesai       : {selesai}")
        print(f"Tugas belum selesai : {belum_selesai}")
        print(f"Total tugas         : {len(todo_list)}")

    # 6. Keluar dari program
    elif pilihan == "6":
        print("Program To-Do List selesai.")
        break

    # Jika menu tidak valid
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-6.")