
# Membuat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()

# Mengisi daftar undangan
print("Masukkan nama undangan (pisahkan dengan koma):")
undangan = set(map(str.strip, input().split(".")))

# Mengisi peserta Webinar A
print("Masukkan peserta Webinar A (pisahkan dengan koma):")
webinar_A = set(map(str.strip, input().split(".")))

# Mengisi peserta Webinar B
print("Masukkan peserta Webinar B (pisahkan dengan koma):")
webinar_B = set(map(str.strip, input().split(".")))

# Menampilkan seluruh peserta
print("=== HASIL DATA WEBINAR ===")

print("Semua peserta:", sorted(webinar_A | webinar_B))

# Peserta yang hadir di kedua webinar
print("Hadir di kedua webinar:",
      sorted(webinar_A & webinar_B))

# Peserta yang hanya hadir di salah satu webinar
print("Hadir di salah satu webinar:",
      sorted(webinar_A ^ webinar_B))

# Undangan yang tidak hadir di webinar mana pun
print("Tidak hadir:",
      sorted(undangan - (webinar_A | webinar_B)))
