# Sistem Informasi Penilaian Mahasiswa

# Fungsi untuk Validasi Teks (Nama)
def validasi_nama(pesan_prompt):
    while True:
        nama = input(pesan_prompt)
        if not nama:
            print("Masukan Tidak Boleh Kosong")
            print()
            continue
            
        if nama[0] == "-":
            print("Masukan Tidak Boleh Minus")
            print()
            continue
            
        ada_angka = False
        for karakter in nama:
            if karakter >= '0' and karakter <= '9':
                ada_angka = True
                break
                
        if ada_angka == True:
            print("Masukan Tidak Boleh Selain Huruf")
            print()
            continue

        return nama

# Fungsi untuk Validasi Angka/Nilai (0-100)
def validasi_nilai(pesan_prompt):
    while True:
        input_nilai = input(pesan_prompt)

        if not input_nilai:
            print("Masukan Tidak Boleh Kosong")
            print()
            continue

        if input_nilai[0] == "-":
            print("Masukan Tidak Boleh Minus")
            print()
            continue
            
        is_angka = True
        for karakter in input_nilai:
            if karakter < '0' or karakter > '9':
                is_angka = False
                break
                
        if not is_angka:
            print("Masukan Tidak Boleh Selain Angka")
            print()
            continue
            
        nilai = int(input_nilai)
        if nilai > 100 or nilai < 0:
            print("Nilai Tidak Boleh Lebih Dari 100 dan kurang dari 0")
            print()
            continue
            
        return nilai

# Fungsi Perhitungan Penilaian Mahasiswa
def hitung_nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
    
    if nilai_akhir >= 85:
        grade = "A"
        status = "Lulus"
    elif nilai_akhir >= 70:
        grade = "B"
        status = "Lulus"
    elif nilai_akhir >= 55:
        grade = "C"
        status = "Lulus"
    else:
        grade = "D"
        status = "Tidak Lulus"
        
    # Menampilkan hasil perhitungan
    print("----------------------------")
    print("| HASIL PENILAIAN MAHASISWA")
    print("|                           ")
    print("| Nama Mahasiswa :", nama)
    print("| Nilai Tugas    :", tugas)
    print("| Nilai UTS      :", uts)
    print("| Nilai UAS      :", uas)
    print("| Nilai Akhir    :", nilai_akhir)
    print("| Grade          :", grade)
    print("| Status         :", status)
    print("----------------------------")

nama = validasi_nama("Masukkan Nama Mahasiswa: ")
tugas = validasi_nilai("Masukkan Nilai Tugas (0-100): ")
uts = validasi_nilai("Masukkan Nilai UTS (0-100): ")
uas = validasi_nilai("Masukkan Nilai UAS (0-100): ")

hitung_nilai_mahasiswa(nama, tugas, uts, uas)