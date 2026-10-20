nilaiA = 0
nilaiB = 0
nilaiC = 0
nilaiD = 0
nilaiE = 0

totalNilai = 0
nilaiTertinggi = 0
namaTertinggi = ""
nilaiTerendah = 100
namaTerendah = ""


# ==== PERULANGAN SEMUA ====
for i in range(10):

    print("\nMahasiswa ke - ", i + 1)

    # akan diulang jika kosong/hanya angka
    while True:
        nama = input("Masukkan Nama Mahasiswa = ")
        namaAngka = True

        for karakter in nama:
            if (karakter < "0" or karakter > "9") and karakter != "-":
                namaAngka = False

        if nama != "" and namaAngka == False:
            break
        print("Maaf, Yang Anda Inputkan Itu Salah")

    # akan diulang jika kosong/bukan angka/negatif
    while True:
        nilaiTugas = input("Masukkan Nilai Tugas Mahasiswa = ")
        angka = nilaiTugas != ""
        for karakter in nilaiTugas:
            if karakter < "0" or karakter > "9":
                angka = False
        if angka == True:
            nilaiTugas = float(nilaiTugas)
            break
        print("Maaf, Yang Anda Inputkan Itu Salah")

    # diulang jika kosong/bukan angka/negatif
    while True:
        uts = input("Masukkan Nilai UTS Mahasiswa = ")
        angka = uts != ""
        for karakter in uts:
            if karakter < "0" or karakter > "9":
                angka = False
        if angka == True:
            uts = float(uts)
            break
        print("Maaf, Yang Anda Inputkan Itu Salah")

    # diulang jika kosong/bukan angka/negatif
    while True:
        uas = input("Masukkan Nilai UAS Mahasiswa = ")
        angka = uas != ""
        for karakter in uas:
            if karakter < "0" or karakter > "9":
                angka = False
        if angka == True:
            uas = float(uas)
            break
        print("Maaf, Yang Anda Inputkan Itu Salah")

    # ==== PENJUMLAHAN NILAI AKHIR NYA =====
    akhir = round((nilaiTugas * 0.3) + (uts * 0.3) + (uas * 0.4))

    # ==== PENGKONDISIAN URUTAN NILAI ====
    if akhir >= 85 and akhir <= 100:
        final = "Selamat Anda Mendapat A"
        nilaiA += 1
    elif akhir >= 75 and akhir <= 84:
        final = "Selamat Anda Mendapat Nilai B"
        nilaiB += 1
    elif akhir >= 65 and akhir <= 74:
        final = "Selamat Anda Mendapat Nilai C"
        nilaiC += 1
    elif akhir >= 50 and akhir <= 64:
        final = "Selamat Anda Mendapat Nilai D"
        nilaiD += 1
    else:
        final = "Maaf, Anda Mendapat Nilai E"
        nilaiE += 1

    # ==== TAMPILAN SEMUA DATA MAHASISWA ====
    print(nama, "| Tugas = ", nilaiTugas, "| UTS = ", uts, "| UAS = ", uas, "| NIlai Akhir Kamu = ", final)

    # ==== CATATAN REKAP DOSEN ====
    totalNilai += akhir

    if akhir > nilaiTertinggi:
        nilaiTertinggi = akhir
        namaTertinggi = nama

    if akhir < nilaiTerendah:
        nilaiTerendah = akhir
        namaTerendah = nama

# ==== TAMPILAN REKAP DOSEN ====
print("\n==== JUMLAH MAHASISWA YANG MENDAPAT NILAI SECARA BERURUTAN ====")
print("Total Nilai A", nilaiA)
print("Total Nilai B", nilaiB)
print("Total Nilai C", nilaiC)
print("Total Nilai D", nilaiD)
print("Total Nilai E", nilaiE)

print("\n==== URUTAN NILAI SELURUH MAHASISWA ====")
print("Total Nilai Tertinggi = ", nilaiTertinggi, "Milik", namaTertinggi)
print("Total Nilai Terendah = ", nilaiTerendah, "Milik", namaTerendah)

print("\n==== RATA - RATA NILAI AKHIR ====")
print("Rata - Rata Nilai Akhir = ", totalNilai / 10)