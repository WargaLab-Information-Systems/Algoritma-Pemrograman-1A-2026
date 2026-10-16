semua_kategori = ""
total = 0
tertinggi = 0
terendah = 100

def valid_nilai(prompt):
    while True:
        nilai = input(prompt)
        if nilai.strip() == "":
            print("Input tidak boleh kosong!")
            continue
        if not nilai.isdigit():
            print("Hanya boleh angka!")
            continue
        nilai = int(nilai)
        if nilai < 0 or nilai > 100:
            print("Nilai 0-100 saja!")
            continue
        return nilai

for i in range(10):
    nama = input("Nama: ")
    while nama.strip() == "":
        print("Nama tidak boleh kosong, ulangi!")
        nama = input("Nama: ")

    tugas = valid_nilai("Nilai tugas: ")
    uts = valid_nilai("Nilai UTS: ")
    uas = valid_nilai("Nilai UAS: ")

    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if akhir >= 85:
        kategori = "A"
    elif akhir >= 75:
        kategori = "B"
    elif akhir >= 65:
        kategori = "C"
    elif akhir >= 50:
        kategori = "D"
    else:
        kategori = "E"

    print(nama, tugas, uts, uas, akhir, kategori)

    semua_kategori += kategori
    total += akhir

    if akhir >= tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir <= terendah:
        terendah = akhir
        nama_terendah = nama

print("Jumlah A:", semua_kategori.count("A"))
print("Jumlah B:", semua_kategori.count("B"))
print("Jumlah C:", semua_kategori.count("C"))
print("Jumlah D:", semua_kategori.count("D"))
print("Jumlah E:", semua_kategori.count("E"))
print("Tertinggi:", tertinggi, nama_tertinggi)
print("Terendah:", terendah, nama_terendah)
print("Rata-rata:", total / 10)