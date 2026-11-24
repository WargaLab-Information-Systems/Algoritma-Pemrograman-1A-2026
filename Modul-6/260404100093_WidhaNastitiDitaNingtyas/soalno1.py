anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik selesai untuk berhenti): ")

    if nama == "selesai":
        break
        
    anggota.append(nama)

print("\nDaftar Anggota:")
for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "- Nama tidak valid")
        continue

    print(nama, "- Nama valid")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan.")

print("\nDaftar Anggota Akhir:", anggota)