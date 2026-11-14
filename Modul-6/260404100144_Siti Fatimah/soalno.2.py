# Input nama asisten awal
asisten = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten.append(nama)

# Mengubah list menjadi tuple
asisten_awal = tuple(asisten)

# Input asisten tambahan
tambahan = input("Masukkan nama asisten tambahan: ")

# Menggabungkan tuple
asisten_akhir = asisten_awal + (tambahan,)

print("Daftar Asisten:", asisten_akhir)

# Input hari tugas
hari = []

while True:
    nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

# Mengubah list menjadi tuple
hari_tugas = tuple(hari)

# Input pengecualian
print("Masukkan Data Pengecualian")
asisten_khusus = input("Nama asisten: ")
hari_khusus = input("Hari pengecualian: ")

# Membuat kombinasi jadwal
print("Jadwal Shift Asisten:")

for nama in asisten_akhir:
    for h in hari_tugas:
        if nama == asisten_khusus and h == hari_khusus:
            continue

        print(nama, "-", h)