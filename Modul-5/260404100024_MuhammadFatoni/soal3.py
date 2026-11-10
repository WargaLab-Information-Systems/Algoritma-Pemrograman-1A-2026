def input_nilai(prompt):
    while True:
            nilai = input(prompt)
            if nilai.strip() == "":
                print("Input tidak boleh kosong!")
            elif nilai.startswith("-"):
                print("Nilai tidak boleh negatif!")
            elif not nilai.replace(".", "", 1).isdigit():
                print("Hanya boleh angka, ini bukan bilangan valid!")
            elif float(nilai) > 100:
                print("Nilai tidak boleh lebih dari 100!")
            else:
                return float(nilai)

def input_nama():
     while True:
            nama = input("Masukkan nama mahasiswa : ")
            if nama.strip() == "":
                print("Input tidak boleh kosong!")
            elif nama.lstrip("-").isdigit():
                print("Tolong jangan input angka, yang diminta di sini adalah berupa teks/nama!")
            elif nama.startswith("-"):
                print("Tanda minus tidak boleh, yang diminta di sini adalah berupa teks/nama!")
            else:
                return nama

def nilai_akhir(nama, tugas, uts, uas):
        akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

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

        print("Nama mahasiswa :", nama)
        print("Nilai tugas    :", tugas)
        print("Nilai UTS      :", uts)
        print("Nilai UAS      :", uas)
        print("Nilai akhir    :", akhir)
        print("Grade          :", grade)
        print("Status         :", status)

nama = input_nama()
tugas = input_nilai("Masukkan nilai tugas : ")
uts = input_nilai("Masukkan nilai UTS : ")
uas = input_nilai("Masukkan nilai UAS : ")

nilai_akhir(nama, tugas, uts, uas)
