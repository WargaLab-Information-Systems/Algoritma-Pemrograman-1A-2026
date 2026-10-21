jumlah_a = jumlah_b = jumlah_c = jumlah_d = jumlah_e = 0
total = 0
tertinggi = -1
terendah = 101

for i in range(10):
    print()
    print("Mahasiswa ke-", i + 1)

    while True:
        nama = input("Nama: ")
        ada_huruf = False   # ada karakter selain spasi?
        ada_angka = False   # ada angka di dalam nama?
        for karakter in nama:
            if karakter != " ":
                ada_huruf = True
            if karakter in "0123456789":
                ada_angka = True

        if nama == "" or not ada_huruf:
            print("nama tidak boleh kosong!")
        elif ada_angka:
            print("nama tidak boleh mengandung angka!")
        else:
            break

    for jenis in ["tugas", "UTS", "UAS"]:
        while True:
            teks = input("Nilai " + jenis + ": ")

            # cek apakah semua karakter adalah angka 0-9
            semua_angka = True
            for karakter in teks:
                if karakter not in "0123456789":
                    semua_angka = False

            if teks == "":
                print("nilai tidak boleh kosong!")
            elif teks[0] == "-":
                print("nilai tidak boleh negatif!")
            elif not semua_angka:
                print("nilai harus berupa angka bulat, bukan huruf/simbol/spasi!")
            elif int(teks) > 100:
                print("nilai harus antara 0 sampai 100!")
            else:
                break

        # simpan ke variabel sesuai jenisnya
        if jenis == "tugas":
            tugas = int(teks)
        elif jenis == "UTS":
            uts = int(teks)
        else:
            uas = int(teks)

    # nilai akhir (30% tugas + 30% UTS + 40% UAS), dibulatkan dengan //
    akhir = (tugas * 3 + uts * 3 + uas * 4 + 5) // 10

    if akhir >= 85:
        kategori = "A"
        jumlah_a += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_b += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1

    print(nama, "| Tugas:", tugas, "| UTS:", uts, "| UAS:", uas,
          "| Akhir:", akhir, "| Nilai:", kategori)

    total += akhir
    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print()
print("Jumlah A:", jumlah_a)
print("Jumlah B:", jumlah_b)
print("Jumlah C:", jumlah_c)
print("Jumlah D:", jumlah_d)
print("Jumlah E:", jumlah_e)
print("Tertinggi:", tertinggi, "-", nama_tertinggi)
print("Terendah:", terendah, "-", nama_terendah)
print("Rata-rata:", (total + 5) // 10)