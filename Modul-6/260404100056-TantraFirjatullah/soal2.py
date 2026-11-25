def masukkan_nama():
    asisten = []
    print()
    print("Ketik 'cukup' untuk selesai.")
    while True:
        data = input("Masukkan Nama: ")
        if data.lower() == "cukup":
            break
        asisten.append(data)
    return asisten

asisten = tuple(masukkan_nama()) + (input("Masukkan Nama Tambahan: "),)

# hariTugas = []
# print()
# print("Ketik 'cukup' untuk selesai.")
# while True:
#     hari = input("Masukkan nama hari tugas: ")
#     if hari.lower() == "cukup":
#         break
#     hariTugas.append(hari)

hariTugas = ("Senin", "Selasa", "Rabu")

print()
asistenKecuali = input("Masukkan nama asisten pengecualian: ")
hariKecuali = input("Masukkan hari pengecualian: ")

jadwal = []
for nama in asisten:
    for hari in hariTugas:
        if nama.lower() == asistenKecuali.lower() and hari.lower() == hariKecuali.lower():
            continue
        jadwal.append((nama, hari))

print()
for i in range(len(jadwal)):
    nama, hari = jadwal[i]
    print(f"{i + 1}. {nama} - {hari}")
print(f"Total shift: {len(jadwal)}")
