# Membuat tiga set kosong
undangan = set()
webinar_a = set()
webinar_b = set()

# Input daftar undangan
teks = input("Masukkan daftar undangan (pisahkan dengan koma): ").strip()
undangan = set(map(str.strip, teks.split(","))) - {""}

# Input peserta Webinar A
teks = input("Masukkan peserta Webinar A (pisahkan dengan koma): ").strip()
webinar_a = set(map(str.strip, teks.split(","))) - {""}

# Input peserta Webinar B
teks = input("Masukkan peserta Webinar B (pisahkan dengan koma): ").strip()
webinar_b = set(map(str.strip, teks.split(","))) - {""}

# Operasi himpunan
semua_peserta = webinar_a | webinar_b
kedua_webinar = webinar_a & webinar_b
satu_webinar = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta

# Menampilkan hasil
print("\n HASIL DATA WEBINAR ")

print("Semua peserta:", semua_peserta)
print("Peserta kedua webinar:", kedua_webinar)
print("Peserta hanya satu webinar:", satu_webinar)
print("Undangan tidak hadir:", tidak_hadir)