jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0
nilai_tertinggi = 0
nama_tertinggi = ""
nilai_terendah = 0
nama_terendah = ""

for i in range(1, 11, 2):
    print("=== Mahasiswa ke-", i, "===")

    while 1:
        nama = input("Nama : ")
        if nama == "":
            print("Nama tidak boleh kosong, ulangi")
            continue

        ada_angka = False
        ada_huruf = False
        for huruf in nama:
            if huruf >= "0" and huruf <= "9":
                ada_angka = True
            if huruf != " ":
                ada_huruf = True

        if ada_huruf == False:                     
            print("Nama tidak boleh kosong, ulangi")
            continue
        if ada_angka:
            print("Nama tidak boleh mengandung angka, ulangi")
            continue
        break
    
    poin = 0                                       
    for k in range(1, 4):

        if k == 1:
            jenis = "tugas"
            bobot = 30
        elif k == 2:
            jenis = "UTS"
            bobot = 30
        else:
            jenis = "UAS"
            bobot = 40

        while 1:
            teks = input("Nilai " + jenis + " : ")
            if teks == "":
                print("Nilai tidak boleh kosong, ulangi")
                continue

            angka_valid = True
            jumlah_angka = 0
            posisi = 0
            for huruf in teks:
                posisi += 1
                if posisi == 1 and huruf == "-":
                    pass
                elif huruf >= "0" and huruf <= "9":
                    jumlah_angka += 1
                else:
                    angka_valid = False

            if angka_valid == False or jumlah_angka == 0:
                print("Nilai harus berupa bilangan bulat, ulangi")
                continue

            nilai = int(teks)
            if nilai < 0:
                print("Nilai tidak boleh negatif, ulangi")
                continue
            if nilai > 100:
                print("Nilai tidak boleh lebih dari 100, ulangi")
                continue
            break

        poin += nilai * bobot

        if k == 1:
            tugas = nilai
        elif k == 2:
            uts = nilai
        else:
            uas = nilai

    akhir = poin / 100                             

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("--- Hasil ---")
    print("Nama        :", nama)
    print("Nilai tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai akhir :", akhir)
    print("Kategori    :", kategori)
    print()

    total_nilai += akhir

    if i == 1:
        nilai_tertinggi = akhir
        nama_tertinggi = nama
        nilai_terendah = akhir
        nama_terendah = nama
    else:
        if akhir > nilai_tertinggi:
            nilai_tertinggi = akhir
            nama_tertinggi = nama
        if akhir < nilai_terendah:
            nilai_terendah = akhir
            nama_terendah = nama

rata_rata = total_nilai / 10

print("===== REKAP KELAS =====")
print("Jumlah nilai A :", jumlah_A)
print("Jumlah nilai B :", jumlah_B)
print("Jumlah nilai C :", jumlah_C)
print("Jumlah nilai D :", jumlah_D)
print("Jumlah nilai E :", jumlah_E)
print("Nilai akhir tertinggi :", nilai_tertinggi, "oleh", nama_tertinggi)
print("Nilai akhir terendah  :", nilai_terendah, "oleh", nama_terendah)
print("Rata-rata nilai akhir :", rata_rata)