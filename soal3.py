a = b = c = d = e = 0
total = 0
tertinggi = -1
terendah = 101

for i in range(10):
    print("Mahasiswa ke-", i + 1)
    nama = input("Nama : ")
    nilaiTugas = float(input("nilaiTugas : "))
    uts = float(input("UTS : "))
    uas = float(input("UAS : "))

    akhir = round(nilaiTugas * 0.3 + uts * 0.3 + uas * 0.4, 2)

    if akhir >= 85:
        kategori = "A"
        a = a + 1
    elif akhir >= 75:
        kategori = "B"
        b = b + 1
    elif akhir >= 65:
        kategori = "C"
        c = c + 1
    elif akhir >= 50:
        kategori = "D"
        d = d + 1
    else:
        kategori = "E"
        e = e + 1

    print(nama, "| nilaiTugas:", nilaiTugas, "| UTS:", uts, "| UAS:", uas,
          "| Akhir:", akhir, "| Kategori:", kategori)
    print()

    total = total + akhir

    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("Jumlah A:", a)
print("Jumlah B:", b)
print("Jumlah C:", c)
print("Jumlah D:", d)
print("Jumlah E:", e)
print("Nilai tertinggi:", tertinggi, "(", nama_tertinggi, ")")
print("Nilai terendah :", terendah, "(", nama_terendah, ")")
print("Rata-rata      :", round(total / 10, 2))