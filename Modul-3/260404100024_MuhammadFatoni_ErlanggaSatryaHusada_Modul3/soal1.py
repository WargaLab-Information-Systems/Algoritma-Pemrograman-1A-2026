jumlah = 0
total_pendapatan = 0
total_jarak = 0
terjauh = 0

def input_jarak():
    while True:
        nilai = input("Masukkan jarak (km): ")
        if nilai.strip() == "":
            print("Input tidak boleh kosong!")
            continue
        if not nilai.lstrip("-").isdigit():
            print("Hanya boleh angka!")
            continue
        return int(nilai)

jarak = input_jarak()

while jarak != 0:
    if jarak < 0:
        print("Jarak tidak valid, ulangi!")
    else:
        jumlah += 1

        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + (jarak - 5) * 1000
        else:
            tarif = 13000 + (jarak - 15) * 500

        if jumlah % 5 == 0:
            tarif = tarif // 2

        total_pendapatan += tarif
        total_jarak += jarak
        if jarak > terjauh:
            terjauh = jarak

    jarak = input_jarak()

print("Jumlah penumpang:", jumlah)
print("Total pendapatan: Rp", total_pendapatan)
print("Jarak terjauh:", terjauh, "km")
if jumlah > 0:
    print("Rata-rata jarak:", total_jarak / jumlah, "km")