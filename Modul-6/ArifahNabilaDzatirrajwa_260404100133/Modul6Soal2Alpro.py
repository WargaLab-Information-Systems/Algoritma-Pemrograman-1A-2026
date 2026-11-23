asisten_awal = []
while True:
    nama = input("Masukkan nama asisten laboratorium: ")
    if nama == "cukup":
        break
    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)
tambahan = input("Masukkan asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

hari_tugas = []
while True:
    hari = input("Masukkan hari tugas: ")
    if hari == "cukup":
        break
    hari_tugas.append(hari)

hari_tugas = tuple(hari_tugas)
pengecualian_asisten = input("Nama asisten yang dikecualikan: ")
pengecualian_hari = input("Hari yang dikecualikan: ")

print("Jadwal Shift Asisten Laboratorium:")

for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == pengecualian_asisten and hari == pengecualian_hari:
            continue
        print(asisten, "-", hari)