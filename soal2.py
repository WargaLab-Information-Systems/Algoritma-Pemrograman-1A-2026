asisten = []
while True:
    nama = input("Nama asisten: ")
    if nama == "cukup":
        break
    asisten.append(nama)

asisten_awal = tuple(asisten)
daftar_asisten = list(asisten_awal)

tambahan = input("Asisten tambahan: ")
daftar_asisten.append(tambahan)

hari = []
while True:
    nama_hari = input("Nama hari: ")
    if nama_hari == "cukup":
        break
    hari.append(nama_hari)

hari_tugas = tuple(hari)

pengecualian = (
    input("Nama pengecualian: "),
    input("Hari pengecualian: ")
)

jadwal = []
for a in daftar_asisten:
    for h in hari_tugas:
        if (a, h) != pengecualian:
            jadwal.append((a, h))

for data in jadwal:
    print(data)