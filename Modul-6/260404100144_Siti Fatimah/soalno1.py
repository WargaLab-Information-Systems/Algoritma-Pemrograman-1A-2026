anggota = []

# Input nama anggota
while True:
    nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

print("Daftar Anggota:", anggota)

# Memeriksa validitas nama
print("Hasil Pemeriksaan Nama:")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

# Menghapus nama penyusup
penyusup = input("Masukkan nama yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan dalam pendaftaran.")

print("Daftar Anggota Akhir:", anggota)