def tampilkan_menu():
    print()
    print("Menu To-do List")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Hitung tugas selesai & belum")
    print("6. Keluar")

def tambah_tugas(tugas):
    nama = input("Nama tugas: ")
    if nama == "":
        print("Nama tugas tidak boleh kosong.")
    elif nama in tugas:
        print(f"Tugas '{nama}' sudah ada.")
    else:
        tugas[nama] = "Belum"
        print(f"Tugas '{nama}' ditambahkan.")

def tampilkan_tugas(tugas):
    if len(tugas) == 0:
        print("Belum ada tugas.")
        return
    print()
    print("Daftar Tugas:")
    nomor = 1
    for nama, status in tugas.items():
        print(f"{nomor}. {nama} - {status}")
        nomor += 1

def tandai_selesai(tugas):
    nama = input("Nama tugas yang diselesaikan: ")
    if nama in tugas:
        tugas[nama] = "Selesai"
        print(f"Tugas '{nama}' ditandai selesai.")
    else:
        print(f"Tugas '{nama}' tidak ditemukan.")

def hapus_tugas(tugas):
    nama = input("Nama tugas yang dihapus: ")
    if nama in tugas:
        del tugas[nama]
        print(f"Tugas '{nama}' dihapus.")
    else:
        print(f"Tugas '{nama}' tidak ditemukan.")

def hitung_status(tugas):
    selesai = 0
    belum = 0
    for status in tugas.values():
        if status == "Selesai":
            selesai += 1
        else:
            belum += 1
    return selesai, belum

def tampilkan_hitungan(tugas):
    selesai, belum = hitung_status(tugas)
    print(f"Tugas selesai : {selesai}")
    print(f"Tugas belum : {belum}")
    print(f"Total tugas : {len(tugas)}")

def main():
    tugas = {}
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
            tambah_tugas(tugas)
        elif pilihan == "2":
            tampilkan_tugas(tugas)
        elif pilihan == "3":
            tandai_selesai(tugas)
        elif pilihan == "4":
            hapus_tugas(tugas)
        elif pilihan == "5":
            tampilkan_hitungan(tugas)
        elif pilihan == "6":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")
            continue

if __name__ == "__main__":
    main()
