asisten = []

while True:
    nama = input("Masukkan nama asisten (ketik 'cukup' untuk selesai): ").strip()

    if nama.lower() == "cukup":
        break
    elif nama == "":
        print("Peringatan: Nama tidak boleh kosong!")
        continue
    elif not nama.replace(" ", "").isalpha():
        print("Peringatan: Nama hanya boleh berisi huruf!")
        continue

    asisten.append(nama)

asisten_awal = tuple(asisten)

while True:
    tambahan = input("Masukkan nama asisten tambahan: ").strip()

    if tambahan == "":
        print("Peringatan: Nama tidak boleh kosong!")
    elif not tambahan.replace(" ", "").isalpha():
        print("Peringatan: Nama hanya boleh berisi huruf!")
    else:
        break

asisten_akhir = asisten_awal + (tambahan,)

hari = []

while True:
    nama_hari = input("Masukkan hari (ketik 'cukup' untuk selesai): ").strip()

    if nama_hari.lower() == "cukup":
        break
    elif nama_hari == "":
        print("Peringatan: Hari tidak boleh kosong!")
        continue
    elif not nama_hari.replace(" ", "").isalpha():
        print("Peringatan: Hari hanya boleh berisi huruf!")
        continue

    hari.append(nama_hari)

hari_akhir = tuple(hari)

while True:
    pengecualian_asisten = input("Masukkan nama asisten yang dikecualikan: ").strip()

    if pengecualian_asisten == "":
        print("Peringatan: Nama tidak boleh kosong!")
    elif not pengecualian_asisten.replace(" ", "").isalpha():
        print("Peringatan: Nama hanya boleh berisi huruf!")
    else:
        break

while True:
    pengecualian_hari = input("Masukkan hari yang dikecualikan: ").strip()

    if pengecualian_hari == "":
        print("Peringatan: Hari tidak boleh kosong!")
    elif not pengecualian_hari.replace(" ", "").isalpha():
        print("Peringatan: Hari hanya boleh berisi huruf!")
    else:
        break

print("\nJadwal Shift Asisten Laboratorium:")

for nama in asisten_akhir:
    for nama_hari in hari_akhir:
        if nama == pengecualian_asisten and nama_hari == pengecualian_hari:
            continue

        print(nama, "-", nama_hari)