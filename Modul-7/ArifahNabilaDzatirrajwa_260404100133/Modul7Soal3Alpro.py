undangan = set()
webinar_digital = set()
webinar_teknologi = set()

print(" DATA UNDANGAN DAN PESERTA WEBINAR ")
jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input("Masukkan nama undangan: ")
    undangan.add(nama)

print(" PESERTA WEBINAR DIGITAL ")
jumlah = int(input("Masukkan jumlah peserta Webinar Digital: "))

for i in range(jumlah):
    nama = input("Masukkan nama peserta: ")
    webinar_digital.add(nama)

print(" PESERTA WEBINAR TEKNOLOGI ")
jumlah = int(input("Masukkan jumlah peserta Webinar Teknologi: "))

for i in range(jumlah):
    nama = input("Masukkan nama peserta: ")
    webinar_teknologi.add(nama)

semua_peserta = webinar_digital | webinar_teknologi

peserta_keduanya = webinar_digital & webinar_teknologi

peserta_satu = webinar_digital ^ webinar_teknologi

tidak_hadir = undangan - semua_peserta

jumlah_webinar_digital = len(webinar_digital)
jumlah_webinar_teknologi = len(webinar_teknologi)
jumlah_semua = len(semua_peserta)

print(" HASIL PENGOLAHAN DATA WEBINAR")

print("Seluruh peserta kedua webinar:")
print(semua_peserta)

print("Peserta yang hadir di kedua webinar:")
print(peserta_keduanya)

print("Peserta yang hanya hadir di salah satu webinar:")
print(peserta_satu)

print("Undangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)

print(" REKAP JUMLAH PESERTA WEBINAR ")
print("Jumlah peserta Webinar Digital:", jumlah_webinar_digital)
print("Jumlah peserta Webinar Teknologi:", jumlah_webinar_teknologi)
print("Total peserta unik:", jumlah_semua)
