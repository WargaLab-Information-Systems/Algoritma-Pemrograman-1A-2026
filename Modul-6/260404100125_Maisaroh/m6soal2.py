asistenAwal = []  # Memasukkan nama asisten awal

while True:
    nama = input("masukkan nama asisten (ketik cukup): ")

    if nama == "cukup":
        break

    asistenAwal.append(nama)

asistenAwal = tuple(asistenAwal)  # Mengunci data asisten awal
tambahan = input("\nmasukkan nama asisten tambahan: ")  # Memasukkan asisten tambahan
asistenAkhir = asistenAwal + (tambahan,)  # Menggabungkan data asisten

hari = []   # Memasukkan nama hari tugas

while True:
    namaHari = input("masukkan hari tugas (ketik cukup): ")

    if namaHari == "cukup":
        break

    hari.append(namaHari)

hari = tuple(hari)   # Mengunci data hari

namaPengecualian = input("\nnama asisten pengecualian: ")  # Memasukkan pengecualian
hariPengecualian = input("hari pengecualian: ")

print("\n===== JADWAL SHIFT ASISTEN =====")  # Membuat kombinasi jadwal

for asisten in asistenAkhir:
    for namaHari in hari:

        if asisten == namaPengecualian and namaHari == hariPengecualian:
            continue

        print(asisten, "-", namaHari)