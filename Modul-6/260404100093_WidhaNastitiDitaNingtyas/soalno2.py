asisten = []

while True:
    nama = input("Masukkan nama asisten (ketik cukup): ")

    if nama.lower() == "cukup":
        break

    asisten.append(nama)

    asisten_awal = tuple(asisten)

    tambahan = input("\nMasukkan nama asisten tambahan: ")

    asisten_akhir = asisten_awal + (tambahan,)

hari = []

while True:
    nama_hari = input("Masukkan hari tugas (ketik cukup): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

hari_tugas = tuple(hari)

pengecualian_asisten = input("\nMasukkan nama asisten yang dikecualikan: ")
pengecualian_hari = input("Masukkan hari yang dikecualikan: ")

print("\nJadwal Shift Asisten:")

for nama in asisten_akhir:
    for hari in hari_tugas:
 
        if nama == pengecualian_asisten and hari == pengecualian_hari:
            continue

        print(nama, "-", hari)