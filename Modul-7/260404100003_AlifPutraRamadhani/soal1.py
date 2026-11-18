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

# Fungsi validasi pilihan menu (1-6)
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
        if int(angka) < 1 or int(angka) > 6:
            print("Pilihan menu hanya 1-6!")
            continue
        return angka
    
# Program To-Do List
todo_list = {}

while True:
    print()
    print("<===== MENU TO-DO LIST =====>")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas") 
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai & Belum Selesai")
    print("6. Keluar")
    print() 
    pilihan = validasi_angka("Pilih menu (1-6): ")

    if pilihan == "1":
        print()
        print("Ketik 'sudah' untuk keluar dari menu penambahan tugas.")
        while True:
            tugas = validasi_teks("Masukkan nama tugas: ")
            if tugas.lower() == "sudah":
                print("program selesai menambahkan tugas")
                break
            if tugas in todo_list:
                print("Tugas tersebut sudah ada di dalam daftar.")
            else:
                todo_list[tugas] = "Belum Selesai"
                print("Tugas '" + tugas + "' berhasil ditambahkan.")

    elif pilihan == "2":
        print()
        if len(todo_list) == 0:
            print("Daftar tugas masih kosong.")
        else:
            print("--- DAFTAR TUGAS ---")
            for nama in todo_list:
                print(nama.ljust(20), " | Status :", todo_list[nama].ljust(15))

    elif pilihan == "3":
        print()
        print("Ketik 'selesai' untuk keluar dari menu menandai tugas selesai.")
        while True:
            tugas = validasi_teks("Masukkan nama tugas yang selesai: ")
            if tugas.lower() == "selesai":
                print("program selesai menandai tugas selesai")
                break
            try:
                # Cek dulu apakah key ada dengan mengaksesnya
                status_lama = todo_list[tugas]
                todo_list[tugas] = "Selesai"
                print("Tugas '" + tugas + "' ditandai Selesai.")
            except KeyError:
                print("Error ditangani: Tugas '" + tugas + "' tidak ditemukan!")

    elif pilihan == "4":
        print()
        print("Ketik 'selesai' untuk keluar dari menu penghapusan tugas.")
        while True:
            tugas = validasi_teks("Masukkan nama tugas yang ingin dihapus: ")
            if tugas.lower() == "selesai":
                print("program selesai menghapus tugas")
                break
            try:
                del todo_list[tugas]
                print("Tugas '" + tugas + "' berhasil dihapus.")
            except KeyError:
                print("Error ditangani: Tugas '" + tugas + "' tidak ada di daftar!")

    elif pilihan == "5":
        print()
        selesai = 0
        belum = 0
        for status in todo_list.values():
            if status == "Selesai":
                selesai = selesai + 1
            else:
                belum = belum + 1
        print("Jumlah tugas Selesai         :", selesai)
        print("Jumlah tugas Belum Selesai   :", belum)
        print("Total tugas                  :", len(todo_list))

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak valid!")