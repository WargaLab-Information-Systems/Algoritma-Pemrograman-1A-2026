def baca_nama():
    while 1:
        nama = input("Nama        : ")
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

        return nama

def baca_nilai(jenis):
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

        return nilai

def hitung_nilai(nama, tugas, uts, uas):
    akhir = (30 * tugas + 30 * uts + 40 * uas) / 100      

    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print()
    print("===== HASIL PERHITUNGAN =====")
    print("Nama        :", nama)
    print("Nilai tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai akhir :", akhir)
    print("Grade       :", grade)
    print("Status      :", status)

nama = baca_nama()
tugas = baca_nilai("tugas")
uts = baca_nilai("UTS  ")
uas = baca_nilai("UAS  ")

hitung_nilai(nama, tugas, uts, uas)