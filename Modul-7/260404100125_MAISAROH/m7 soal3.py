undangan = set()
webinarA = set()
webinarB = set()

print("===== INPUT DATA UNDANGAN =====")
data = input("Masukkan nama undangan (pisahkan dengan koma): ")
undangan = set(nama.strip() for nama in data.split(",") if nama.strip())

print("\n===== INPUT PESERTA WEBINAR A =====")
data = input("Masukkan peserta Webinar A (pisahkan dengan koma): ")
webinarA = set(nama.strip() for nama in data.split(",") if nama.strip())

print("\n===== INPUT PESERTA WEBINAR B =====")
data = input("Masukkan peserta Webinar B (pisahkan dengan koma): ")
webinarB = set(nama.strip() for nama in data.split(",") if nama.strip())

semua_peserta = webinarA | webinarB

peserta_keduanya = webinarA & webinarB

peserta_salah_satu = webinarA ^ webinarB

tidak_hadir = undangan - (webinarA | webinarB)

print("\n===== HASIL DATA WEBINAR =====")
print("semua peserta:", sorted(semua_peserta))
print("peserta kedua webinar:", sorted(peserta_keduanya))
print("peserta salah satu webinar:", sorted(peserta_salah_satu))
print("undangan tidak hadir:", sorted(tidak_hadir))
