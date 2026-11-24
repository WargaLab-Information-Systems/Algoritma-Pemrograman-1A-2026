# Program Pengelolaan Peserta Webinar
# Menggunakan Set (Himpunan)

# Membuat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()

# Input daftar undangan
print("===== INPUT DAFTAR UNDANGAN =====")
nama = input("Masukkan nama undangan (pisahkan dengan koma): ")
undangan.update(nama.split(","))

# Input peserta Webinar A
print("\n===== INPUT PESERTA WEBINAR A =====")
nama = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_A.update(nama.split(","))

# Input peserta Webinar B
print("\n===== INPUT PESERTA WEBINAR B =====")
nama = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_B.update(nama.split(","))

# Menghapus spasi berlebih pada setiap nama
undangan = {nama.strip() for nama in undangan}
webinar_A = {nama.strip() for nama in webinar_A}
webinar_B = {nama.strip() for nama in webinar_B}

# Operasi himpunan
semua_peserta = webinar_A.union(webinar_B)
peserta_keduanya = webinar_A.intersection(webinar_B)
peserta_salah_satu = webinar_A.symmetric_difference(webinar_B)
tidak_hadir = undangan.difference(semua_peserta)

# Menampilkan hasil
print("\n===== HASIL DATA WEBINAR =====")

print("\nSemua peserta Webinar A dan Webinar B:")
print(semua_peserta)

print("\nPeserta yang hadir di kedua webinar:")
print(peserta_keduanya)

print("\nPeserta yang hanya hadir di salah satu webinar:")
print(peserta_salah_satu)

print("\nUndangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)