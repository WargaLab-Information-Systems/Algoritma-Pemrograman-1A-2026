# program pendataan inventaris PC laboratorium

def input_angka(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai == "":
            print("Input tidak boleh kosong.")
        elif "-" in nilai:
            print("Tanda '-' tidak boleh digunakan.")
        elif not nilai.isdigit():
            print("Masukkan angka, bukan teks.")
        else:
            return int(nilai)

def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input tidak boleh kosong.")
        elif "-" in teks:
            print("Tanda '-' tidak boleh digunakan.")
        elif teks.isdigit():
            print("Masukkan teks, bukan angka.")
        else:
            return teks

# fungsi untuk menilai kelayakan PC
def cek_layak(pc):
    status = pc[1]
    ram = int(pc[2])
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

# data inventaris
data_pc = []
jumlah = input_angka("Berapa jumlah PC yang mau diinput? ")

for i in range(jumlah):
    print("")
    print("Data PC ke-" + str(i + 1))
    nama = input_teks("Nama PC: ")
    status = input_teks("Status (Normal/Rusak): ")
    # RAM sengaja TIDAK divalidasi, diterima apa adanya sebagai string
    ram = input("Kapasitas RAM (GB): ")
    data_pc.append([nama, status, ram])

# evaluasi semua PC
print("")
print("Hasil evaluasi:")
for pc in data_pc:
    try:
        hasil = cek_layak(pc)
    except ValueError:
        hasil = "Kacau Format RAM nya mas"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')