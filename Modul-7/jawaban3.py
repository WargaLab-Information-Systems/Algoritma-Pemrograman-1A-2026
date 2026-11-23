undangan = set()
webinar_a = set()
webinar_b = set()

jumlah = int(input("Jumlah nama undangan: "))
for i in range(jumlah):
    nama = input("Nama undangan: ")
    undangan.add(nama)

jumlah = int(input("\nJumlah peserta Webinar A: "))
for i in range(jumlah):
    nama = input("Nama peserta Webinar A: ")
    webinar_a.add(nama)

jumlah = int(input("\nJumlah peserta Webinar B: "))
for i in range(jumlah):
    nama = input("Nama peserta Webinar B: ")
    webinar_b.add(nama)

semua_peserta = webinar_a | webinar_b
peserta_keduanya = webinar_a & webinar_b
peserta_satu_webinar = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta

print("\nSemua peserta:", semua_peserta)
print("Hadir di kedua webinar:", peserta_keduanya)
print("Hadir hanya di salah satu webinar:", peserta_satu_webinar)
print("Undangan yang tidak hadir:", tidak_hadir)