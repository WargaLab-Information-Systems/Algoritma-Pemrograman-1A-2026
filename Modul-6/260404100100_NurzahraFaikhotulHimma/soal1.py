anggota = []

while True:
    nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

    if nama == "selesai":
        break

    anggota.append(nama)

print("\nDaftar anggota:")
for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "- Nama tidak valid")
    else:
        print(nama, "- Nama valid")

penyusup = input("\nMasukkan nama penyusup yang akan dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan.")

print("\nDaftar anggota akhir:", anggota)