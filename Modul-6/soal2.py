# program penjadwalan shift asisten laboratorium

def input_teks(pesan):
    while True:
        teks = input(pesan).strip()

        if teks == "":
            print("Input tidak boleh kosong.")
        elif "-" in teks:
            print("Tanda '-' tidak boleh digunakan.")
        elif teks.isdigit():
            print("Masukkan teks, bukan angka.")
        else:
            return teks


# 1. input nama asisten awal sampai ketik "cukup"
asisten_list = []
nama = input_teks("Masukkan nama asisten awal (ketik cukup untuk berhenti): ")
while nama != "cukup":
    asisten_list.append(nama)
    nama = input_teks("Masukkan nama asisten awal (ketik cukup untuk berhenti): ")

# kunci jadi tuple supaya tidak bisa diubah
asisten_awal = tuple(asisten_list)

# 2. input satu asisten tambahan, lalu gabung ke tuple baru
print("")
tambahan = input_teks("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

# 3. input hari tugas sampai ketik "cukup"
print("")
hari_list = []
hari = input_teks("Masukkan hari tugas (ketik cukup untuk berhenti): ")
while hari != "cukup":
    hari_list.append(hari)
    hari = input_teks("Masukkan hari tugas (ketik cukup untuk berhenti): ")

# kunci jadi tuple juga
hari_tugas = tuple(hari_list)

# 4. input pengecualian
print("")
asisten_libur = input_teks("Masukkan nama asisten pengecualian: ")
hari_libur = input_teks("Masukkan hari pengecualian: ")

# 5. pasangkan setiap asisten dengan setiap hari
print("")
print("Jadwal shift:")
for a in asisten_akhir:
    for h in hari_tugas:
        # kalau sama dengan pengecualian, dilewati
        if a == asisten_libur and h == hari_libur:
            continue
        print(a, "-", h)