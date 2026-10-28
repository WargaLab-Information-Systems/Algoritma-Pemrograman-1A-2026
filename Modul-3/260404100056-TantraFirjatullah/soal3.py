mahasiswa = []
totalA, totalB, totalC, totalD, totalE, totalSemua = 0, 0, 0, 0, 0, 0

for i in range(3):
    while True:
        nama = input(f"Masukkan nama mahasiswa {i + 1}: ")
        if nama != "":
            break
        else:
            print("Nama tidak boleh kosong!")

    while True:
        try:
            tugas = float(input("Nilai tugas: "))
        except ValueError as e:
            print(f"Harus berupa angka! {e}")
            continue
        if tugas < 0 or tugas > 100:
            print("Nilai harus antara 0 dan 100!")
            continue
        break

    while True:
        try:
            uts = float(input("Nilai UTS: "))
        except ValueError:
            print("Harus berupa angka!")
            continue
        if uts < 0 or uts > 100:
            print("Nilai harus antara 0 dan 100!")
            continue
        break

    while True:
        try:
            uas = float(input("Nilai UAS: "))
        except ValueError:
            print("Harus berupa angka!")
            continue
        if uas < 0 or uas > 100:
            print("Nilai harus antara 0 dan 100!")
            continue
        break

    total = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if total >= 85:
        kategoriNilai = "A"
        totalA += 1
    elif total >= 75:
        kategoriNilai = "B"
        totalB += 1
    elif total >= 65:
        kategoriNilai = "C"
        totalC += 1
    elif total >= 50:
        kategoriNilai = "D"
        totalD += 1
    else:
        kategoriNilai = "E"
        totalE += 1

    data = {
        "nama": nama,
        "nilaiTugas": tugas,
        "nilaiUTS": uts,
        "nilaiUAS": uas,
        "nilaiAkhir": total,
        "grade": kategoriNilai,
    }
    mahasiswa.append(data)
    print()

for i in range(10):
    print(f"{mahasiswa[i]['nama']} - {mahasiswa[i]['nilaiTugas']} - {mahasiswa[i]['nilaiUTS']} - {mahasiswa[i]['nilaiUAS']} - {mahasiswa[i]['nilaiAkhir']} - {mahasiswa[i]['grade']}")

print()

tertinggi = mahasiswa[0]
terendah = mahasiswa[0]

for m in mahasiswa:
    totalSemua += m["nilaiAkhir"]

    if m["nilaiAkhir"] > tertinggi["nilaiAkhir"]:
        tertinggi = m
    if m["nilaiAkhir"] < terendah["nilaiAkhir"]:
        terendah = m

print(f"Banyak mahasiswa memperoleh Nilai A: {totalA} orang")
print(f"Banyak mahasiswa memperoleh Nilai B: {totalB} orang")
print(f"Banyak mahasiswa memperoleh Nilai C: {totalC} orang")
print(f"Banyak mahasiswa memperoleh Nilai D: {totalD} orang")
print(f"Banyak mahasiswa memperoleh Nilai E: {totalE} orang")
print(f"Mahasiswa bernama {tertinggi['nama']}, memperoleh nilai akhir tertinggi dikelas sebesar {tertinggi['nilaiAkhir']:.1f}")
print(f"Mahasiswa bernama {terendah['nama']}, memperoleh nilai akhir terendah dikelas sebesar {terendah['nilaiAkhir']:.1f}")
print(f"Rata-rata nilai akhir: {totalSemua / len(mahasiswa):.2f}")
print()
