undangan = set()
webinar_a = set()
webinar_b = set()

print("Ketik nama dipisah spasi, contoh: Andi Budi Citra")
print("(satu nama satu kata saja, kosongkan kalau tidak ada)")
print()

daftar_undangan = input("Daftar undangan  : ").strip()
peserta_a = input("Peserta Webinar A: ").strip()
peserta_b = input("Peserta Webinar B: ").strip()

if not daftar_undangan:
    print("Daftar undangan kosong, tidak ada nama yang ditambahkan.")
if not peserta_a:
    print("Daftar peserta Webinar A kosong.")
if not peserta_b:
    print("Daftar peserta Webinar B kosong.")

undangan.update(daftar_undangan.title().split())
webinar_a.add(peserta_a.title())
webinar_b.add(peserta_b.title())

semua_peserta = webinar_a | webinar_b
hadir_keduanya = webinar_a & webinar_b
hanya_satu = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta

print()
print("HASIL")
print("Semua peserta (A dan B)      :", sorted(semua_peserta))
print("Hadir di keduanya            :", sorted(hadir_keduanya))
print("Hanya hadir di salah satu    :", sorted(hanya_satu))
print("Diundang tapi tidak hadir    :", sorted(tidak_hadir))