undangan = set()
webinar_a = set()
webinar_b = set()

print("===== DATA UNDANGAN =====")
undangan.update(input("Masukkan nama undangan (pisahkan dengan koma): ").split(","))

print("\n===== PESERTA WEBINAR A =====")
webinar_a.update(input("Masukkan peserta Webinar A (pisahkan dengan koma): ").split(","))

print("\n===== PESERTA WEBINAR B =====")
webinar_b.update(input("Masukkan peserta Webinar B (pisahkan dengan koma): ").split(","))

semua_peserta = webinar_a | webinar_b

peserta_keduanya = webinar_a & webinar_b

peserta_salah_satu = webinar_a ^ webinar_b

tidak_hadir = undangan - semua_peserta

print("\n===== HASIL WEBINAR =====")
print("Semua peserta:", semua_peserta)
print("Peserta yang hadir di kedua webinar:", peserta_keduanya)
print("Peserta yang hanya hadir di salah satu webinar:", peserta_salah_satu)
print("Undangan yang tidak hadir:", tidak_hadir)