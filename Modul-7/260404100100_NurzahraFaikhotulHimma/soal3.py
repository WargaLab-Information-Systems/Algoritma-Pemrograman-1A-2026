undangan = set()
webinar_a = set()
webinar_b = set()

print("=== INPUT DAFTAR UNDANGAN ===")
jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input("Nama undangan: ")
    undangan.add(nama)

print("\n=== INPUT PESERTA WEBINAR A ===")
jumlah = int(input("Masukkan jumlah peserta: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_a.add(nama)

print("\n=== INPUT PESERTA WEBINAR B ===")
jumlah = int(input("Masukkan jumlah peserta: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_b.add(nama)

print("\n=== HASIL DATA WEBINAR ===")

# Semua peserta dari kedua webinar
semua_peserta = webinar_a | webinar_b
print("Semua peserta:", semua_peserta)

# Peserta yang hadir di kedua webinar
kedua_webinar = webinar_a & webinar_b
print("Hadir di kedua webinar:", kedua_webinar)

# Peserta yang hanya hadir di salah satu webinar
satu_webinar = webinar_a ^ webinar_b
print("Hadir di salah satu webinar:", satu_webinar)

# Undangan yang tidak hadir di webinar mana pun
tidak_hadir = undangan - semua_peserta
print("Undangan tidak hadir:", tidak_hadir)