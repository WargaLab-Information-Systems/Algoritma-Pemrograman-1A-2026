anggota = []  # Membuat list untuk menyimpan nama anggota

while True:   # Memasukkan nama anggota
    nama = input("masukkan nama anggota (ketik selesai): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

print("\n===== PEMERIKSAAN NAMA =====")  # Memeriksa nama anggota

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

hapus = input("\nmasukkan nama yang ingin dihapus: ")  # Menghapus nama penyusup

if hapus in anggota:
    anggota.remove(hapus)
    print("nama berhasil dihapus.")
else:
    print("nama tidak ditemukan.")

print("\ndaftar anggota akhir:", anggota)  # Menampilkan daftar akhir