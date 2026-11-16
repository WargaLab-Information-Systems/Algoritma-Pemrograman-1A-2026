
print("=== SISTEM PENJADWALAN SHIFT LABORATORIUM ===")

# 1. Memasukkan nama asisten awal
asisten = []

while True:
    nama = input("Masukkan nama asisten (ketik cukup untuk berhenti): ")

    if nama == "cukup":
        break

    asisten.append(nama)

# Mengunci data asisten awal menjadi tuple
asisten = tuple(asisten)

# 2. Memasukkan satu asisten tambahan
tambahan = input("\nMasukkan nama asisten tambahan: ")

# Menggabungkan data ke dalam tuple baru
asisten_akhir = asisten + (tambahan,)

# 3. Memasukkan hari tugas
hari = []

while True:
    nama_hari = input("Masukkan hari tugas (ketik cukup untuk berhenti): ")

    if nama_hari == "cukup":
        break

    hari.append(nama_hari)

# Mengunci data hari menjadi tuple
hari = tuple(hari)

# 4. Memasukkan pengecualian
print("\n=== DATA PENGECUALIAN ===")

nama_pengecualian = input("Nama asisten yang dikecualikan: ")
hari_pengecualian = input("Hari yang dikecualikan: ")

# 5. Membuat jadwal shift
print("\n=== JADWAL SHIFT LABORATORIUM ===")

for nama in asisten_akhir:
    for nama_hari in hari:

        if nama == nama_pengecualian and nama_hari == hari_pengecualian:
            continue

        print(nama, "-", nama_hari)

print("\nPenjadwalan selesai!")
