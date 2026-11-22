def cek_nilai(nama, nilaiTugas, uts, uas):
    akhir = round((nilaiTugas * 0.3) + (uts * 0.3) + (uas * 0.4))

    if akhir >= 85 and akhir <= 100:
        final = "Selamat Anda Mendapat A"
    elif akhir >= 75 and akhir <= 84:
        final = "Selamat Anda Mendapat Nilai B"
    elif akhir >= 65 and akhir <= 74:
        final = "Selamat Anda Mendapat Nilai C"
    elif akhir >= 50 and akhir <= 64:
        final = "Selamat Anda Mendapat Nilai D"
    else:
        final = "Maaf, Anda Mendapat Nilai E"

    if final == "D":
        status = "Anda Tidak Lulus"
    else:
        status = "Anda Lulus"

        print("\n==== HASIL PERHITUNGAN ====")
    print("Nama        :", nama)
    print("Nilai Tugas :", nilaiTugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", akhir)
    print("Grade       :", final)
    print("Status      :", status)

def input_nilai(jumlah):
    while True:
        nilai = input(jumlah)
        angka = nilai != ""
        for karakter in nilai:
            if karakter < "0" or karakter > "9":
                angka = False
        if angka == True:
            return float(nilai)
        print("Maaf, Yang Anda Inputkan Itu Salah(Contoh : 80, 90, 100)")

while True:
    nama = input("Masukkan Nama Mahasiswa = ")
    namaAngka = True

    for karakter in nama:
        if (karakter < "0" or karakter > "9") and karakter != "-":
            namaAngka = False

    if nama != "" and namaAngka == False:
        break
    print("Maaf, Yang Anda Inputkan Itu Salah(Contoh : Budi, Siti, DLL)")

nilaiTugas = input_nilai("Masukkan Nilai Tugas Mahasiswa = ")
uts = input_nilai("Masukkan Nilai UTS Mahasiswa = ")
uas = input_nilai("Masukkan Nilai UAS Mahasiswa = ")

cek_nilai(nama, nilaiTugas, uts, uas)