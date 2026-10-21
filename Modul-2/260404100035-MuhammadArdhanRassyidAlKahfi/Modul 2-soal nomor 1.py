# Input kode rahasia 3 digit
while True:
    try:
        input_kode = input("Masukkan kode rahasia 3 digit: ")

        # Mengecek apakah input kosong
        if input_kode.strip() == "":
            print("Input tidak boleh kosong. Silakan masukkan kode 3 digit.")
            continue

        kode = int(input_kode)

        # Mengecek angka negatif
        if kode < 0:
            print("Kode tidak boleh berupa angka negatif. Silakan masukkan kode 3 digit.")
            continue

        # Mengecek apakah kode terdiri dari 3 digit
        if kode < 100 or kode > 999:
            print("Kode harus terdiri dari 3 digit. Silakan masukkan angka 100 sampai 999.")
            continue

        break

    # Menangani input berupa teks atau selain angka
    except ValueError:
        print("Tolong jangan input dengan teks atau kalimat karena yang diminta adalah angka 3 digit.")


# Memisahkan setiap digit
digit1 = kode // 100
digit2 = (kode // 10) % 10
digit3 = kode % 10

# Nilai pelacak awal
pelacak = digit1 * digit3
pelacak_awal = pelacak

# Perubahan tahap pertama
if digit2 % 2 == 1:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - digit2

pelacak_tahap1 = pelacak

# Perubahan tahap kedua
if pelacak % 3 == 0:
    pelacak = pelacak // 3
else:
    pelacak = pelacak * 2

nilai_akhir = pelacak

# Status sKrasny
if nilai_akhir > 50:
    status = "Kategori A"
elif nilai_akhir > 20:
    status = "Kategori B"
else:
    status = "sKrasny Ditolak"

# Menentukan siklus
if nilai_akhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"

# Hasil
print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)
print("Nilai pelacak awal:", pelacak_awal)
print("Nilai pelacak tahap pertama:", pelacak_tahap1)
print("Nilai pelacak tahap kedua:", nilai_akhir)
print("Status sKrasny:", status)
print(siklus)