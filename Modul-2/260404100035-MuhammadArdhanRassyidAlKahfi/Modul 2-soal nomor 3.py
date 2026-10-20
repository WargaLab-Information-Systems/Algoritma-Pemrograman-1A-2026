# Input suhu dan tekanan

# Input suhu
while True:
    try:
        input_suhu = input("Masukkan suhu reaktor (°C): ")

        # Mengecek apakah input kosong
        if input_suhu.strip() == "":
            print("Input suhu tidak boleh kosong. Silakan masukkan angka.")
            continue

        suhu = float(input_suhu)

        # Mengecek angka negatif
        if suhu < 0:
            print("Suhu tidak boleh negatif. Silakan masukkan angka yang benar.")
            continue

        break

    except ValueError:
        print("Tolong jangan input dengan teks atau kalimat karena yang diminta adalah angka.")


# Input tekanan
while True:
    try:
        input_tekanan = input("Masukkan tekanan gas (Bar): ")

        # Mengecek apakah input kosong
        if input_tekanan.strip() == "":
            print("Input tekanan tidak boleh kosong. Silakan masukkan angka.")
            continue

        tekanan = float(input_tekanan)

        # Mengecek angka negatif
        if tekanan < 0:
            print("Tekanan tidak boleh negatif. Silakan masukkan angka yang benar.")
            continue

        break

    except ValueError:
        print("Tolong jangan input dengan teks atau kalimat karena yang diminta adalah angka.")


# Status bahaya reaktor
if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

# Status pompa
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# Hasil
print("Suhu reaktor:", suhu, "°C")
print("Tekanan gas:", tekanan, "Bar")
print("Status bahaya:", status)
print("Status pompa:", pompa)