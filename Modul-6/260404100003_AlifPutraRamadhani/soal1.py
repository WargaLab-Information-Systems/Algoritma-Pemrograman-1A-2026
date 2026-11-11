daftar_anggota = []

while True:
    nama = input("Masukkan nama calon: ")
    if not nama:
        print("Masukan tidak boleh kosong")
        continue
    if nama[0] == "-":
        print("Masukan tidak boleh minus")
        continue

    bukan_huruf = False
    for c in nama:
        if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c == ' '):
            bukan_huruf = True
            break

    if bukan_huruf:
        print("Masukan tidak boleh selain huruf")
        continue
    if nama == "selesai":
        break

    daftar_anggota.append(nama)

print()
print("HASIL EVALUASI CALON ANGGOTA")
for nama in daftar_anggota:
    if nama == "admin" or len(nama) < 4:
        print("Nama '", nama, "' -> TIDAK VALID")
    else:
        print("Nama '", nama, "' -> VALID")

daftar_valid = []
for item in daftar_anggota:
    if item != "admin" and len(item) >= 4:
        daftar_valid.append(item)
daftar_anggota = daftar_valid

print()
penyusup = input("Masukkan nama penyusup: ")
if penyusup in daftar_anggota:
    while penyusup in daftar_anggota:
        daftar_anggota.remove(penyusup)
    print("Nama '", penyusup, "' penyusup berhasil ditemukan dan dihapus.")
else:
    print("Nama '", penyusup, "' tidak ditemukan.")

print("DAFTAR ANGGOTA: ", daftar_anggota)