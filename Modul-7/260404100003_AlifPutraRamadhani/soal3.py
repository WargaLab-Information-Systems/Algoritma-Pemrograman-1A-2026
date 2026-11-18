# Fungsi validasi input teks
def validasi_teks(pesan):
    while True:
        masukan = input(pesan)
        if not masukan:
            print("Masukan tidak boleh kosong!")
            continue
        if masukan[0] == "-":
            print("Masukan tidak boleh minus!")
            continue

        tidak_valid = False
        for c in masukan:
            if not ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == ' '):
                tidak_valid = True
                break

        if tidak_valid:
            print("Masukan hanya boleh huruf atau spasi!")
            continue
        return masukan


# Inisialisasi tiga set awal kosong
undangan = set()
webinar_a = set()
webinar_b = set()

print("<===== INPUT DATA UNDANGAN =====>")
print("Ketik 'selesai' jika sudah selesai memasukkan nama.")
while True:
    nama = validasi_teks("Masukkan nama undangan: ")
    if nama.lower() == "selesai":
        break
    undangan.add(nama)

print()
print("<===== INPUT PESERTA WEBINAR A =====>")
print("Ketik 'selesai' jika sudah selesai memasukkan nama.")
while True:
    nama = validasi_teks("Masukkan nama peserta Webinar A: ")
    if nama.lower() == "selesai":
        break
    webinar_a.add(nama)

print()
print("<===== INPUT PESERTA WEBINAR B =====>")
print("Ketik 'selesai' jika sudah selesai memasukkan nama.")
while True:
    nama = validasi_teks("Masukkan nama peserta Webinar B: ")
    if nama.lower() == "selesai":
        break
    webinar_b.add(nama)

# Operasi himpunan (tanpa perulangan)
semua_peserta = webinar_a.union(webinar_b)
hadir_keduanya = webinar_a.intersection(webinar_b)
hanya_satu_webinar = webinar_a.symmetric_difference(webinar_b)
tidak_hadir = undangan.difference(semua_peserta)

print()
print("<===== HASIL DATA KEHADIRAN WEBINAR =====>")
print("1. Semua peserta dari kedua webinar       :")
print(semua_peserta if semua_peserta else "Tidak ada")
print()
print("2. Peserta yang hadir di kedua webinar    :")
print(hadir_keduanya if hadir_keduanya else "Tidak ada")
print()
print("3. Peserta hanya di salah satu webinar    :")
print(hanya_satu_webinar if hanya_satu_webinar else "Tidak ada")
print()
print("4. Undangan yang tidak hadir sama sekali  :")
print(tidak_hadir if tidak_hadir else "Tidak ada")