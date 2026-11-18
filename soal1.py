tugas = {}


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
    print("MENU TO-DO LIST")
    print("1. Tambah tugas")
    print("2. Lihat semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum")
    print("0. Keluar")
    pilih = input_menu()

    if pilih == 1:
        nama = input_teks("Nama tugas: ")
        if nama in tugas:
            print("Tugas itu sudah ada")
        else:
            tugas[nama] = "Belum"
            print("Tugas berhasil ditambah")

    elif pilih == 2:
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            for nama in tugas:
                print(nama, "-", tugas[nama])

    elif pilih == 3:
        nama = input_teks("Tugas yang sudah selesai: ")
        try:
            if tugas[nama] == "Selesai":
                print("Tugas itu sudah selesai dari tadi")
            else:
                tugas[nama] = "Selesai"
                print("Tugas ditandai selesai")
        except KeyError:
            print("Tugas tidak ditemukan")

    elif pilih == 4:
        nama = input_teks("Tugas yang mau dihapus: ")
        try:
            del tugas[nama]
            print("Tugas dihapus")
        except KeyError:
            print("Tugas tidak ditemukan")

    elif pilih == 5:
        selesai = 0
        belum = 0
        for nama in tugas:
            if tugas[nama] == "Selesai":
                selesai = selesai + 1
            else:
                belum = belum + 1
        print("Sudah selesai:", selesai)
        print("Belum selesai:", belum)

    elif pilih == 0:
        print("SELAMAT TINGGAL")
        break

    else:
        print("Pilihan tidak ada")
