anggota = []

while True:
    nama = input("Masukkan nama: ")
    if nama == "selesai":
        break
    anggota.append(nama)

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

hapus = input("Nama yang ingin dihapus: ")
if hapus in anggota:
    anggota.remove(hapus)
else:
    print("Nama tidak ditemukan")

print(anggota)