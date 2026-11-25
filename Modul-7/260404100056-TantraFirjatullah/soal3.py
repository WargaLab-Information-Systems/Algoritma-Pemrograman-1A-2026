def isi_set(keterangan):
    himpunan = set()
    print()
    print(f"Masukkan nama {keterangan} (kosongkan lalu Enter untuk selesai):")
    while True:
        try:
            nama = input("Nama: ")
            if nama == "":
                break
            himpunan.add(nama)
        except ValueError:
            print("Masukan Tidak Valid")
    return himpunan

def hitung_hasil(undangan, webinar_a, webinar_b):
    semua_peserta = webinar_a | webinar_b
    hadir_keduanya = webinar_a & webinar_b
    hanya_satu = webinar_a ^ webinar_b
    tidak_hadir = undangan - semua_peserta
    return semua_peserta, hadir_keduanya, hanya_satu, tidak_hadir

def tampilkan(judul, himpunan):
    if len(himpunan) == 0:
        print(f"{judul}: (tidak ada)")
    else:
        print(f"{judul}: {', '.join(sorted(himpunan))}")

def main():
    undangan = isi_set("undangan")
    webinar_a = isi_set("peserta Webinar A")
    webinar_b = isi_set("peserta Webinar B")

    semua, keduanya, satu, tidak_hadir = hitung_hasil(undangan, webinar_a, webinar_b)

    print()
    print("Hasil: ")
    tampilkan("Semua peserta kedua webinar ", semua)
    tampilkan("Peserta hadir di keduanya ", keduanya)
    tampilkan("Peserta hanya di salah satu ", satu)
    tampilkan("Undangan tidak hadir di mana pun ", tidak_hadir)

if __name__ == "__main__":
    main()
