def validasi_input(pesan_prompt):
    while True:
        teks = input(pesan_prompt)
        if not teks:
            print("Masukan tidak boleh kosong")
            continue
        if teks[0] == "-":
            print("Masukan tidak boleh minus")
            continue

        bukan_huruf = False
        for c in teks:
            if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c == ' '):
                bukan_huruf = True
                break

        if bukan_huruf:
            print("Masukan tidak boleh selain huruf")
            continue

        return teks

asistenAwal = []
print("Input asisten awal (ketik 'cukup' untuk berhenti):")
while True:
    nama = validasi_input("Masukkan nama asisten awal: ")
    if nama == "cukup":
        break
    asistenAwal.append(nama)

asistenAsli = tuple(asistenAwal)
print("Daftar Asisten Awal:", asistenAsli)

print()
asisten_tambahan = validasi_input("Masukkan nama asisten tambahan: ")
asisten_akhir = asistenAsli + (asisten_tambahan,)
print("Daftar Asisten Akhir:", asisten_akhir)

print()
hari_list = []
hari_valid = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
print("Input hari tugas (ketik 'cukup' untuk berhenti):")
while True:
    hari = validasi_input("Masukkan nama hari tugas: ")
    if hari == "cukup":
        break
    if hari not in hari_valid:
        print("hari yang valid (senin - minggu).")
        continue
    hari_list.append(hari)
daftar_hari = tuple(hari_list)

print()
print("--- INPUT PENGECUALIAN ---")
asistenKhusus = validasi_input("Masukkan nama asisten pengecualian: ")
hariKhusus = validasi_input("Masukkan hari pengecualian: ")

print()
print("Nama Asisten".center(20) + " | " + "Hari Tugas".center(10))
print("-----------------------------------")

for name in asisten_akhir:
    for day in daftar_hari:
        if name == asistenKhusus and day == hariKhusus:
            continue
        print(name.center(20) + " | " + day.center(10))
print()