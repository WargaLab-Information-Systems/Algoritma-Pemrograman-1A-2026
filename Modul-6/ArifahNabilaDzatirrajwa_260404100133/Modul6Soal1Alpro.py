anggota = []
while True:
    nama = input("Masukkan nama anggota: ")
    if nama == "selesai":
        break
    anggota.append(nama)

print("Pemeriksaan Nama Anggota:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

hapus = input("Masukkan nama yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama berhasil dihapus")
else:
    print("Nama tidak ditemukan")

print("Daftar anggota:", anggota)