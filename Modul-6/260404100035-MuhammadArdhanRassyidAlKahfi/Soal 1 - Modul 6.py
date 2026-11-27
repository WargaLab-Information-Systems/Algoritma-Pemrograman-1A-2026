anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik 'selesai' untuk berhenti): ").strip()

    if nama.lower() == "selesai":
        break
    elif nama == "":
        print("Peringatan: Nama tidak boleh kosong!")
        continue
    elif not nama.replace(" ", "").isalpha():
        print("Peringatan: Nama hanya boleh berisi huruf!")
        continue

    anggota.append(nama)

print("\nDaftar Anggota Klub Robotik:")
for nama in anggota:
    print(nama)

print("\nPemeriksaan Nama Anggota:")
for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

while True:
    penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ").strip()

    if penyusup == "":
        print("Peringatan: Nama tidak boleh kosong!")
    elif not penyusup.replace(" ", "").isalpha():
        print("Peringatan: Nama hanya boleh berisi huruf!")
    else:
        break

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Anggota berhasil dihapus!")
else:
    print("Nama tidak ditemukan dalam daftar anggota.")

print("\nDaftar Anggota Setelah Penghapusan:")
print(anggota)