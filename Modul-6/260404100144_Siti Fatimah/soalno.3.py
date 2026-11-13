# Fungsi untuk mengevaluasi kelayakan PC
def evaluasi(status, ram):
    if status == "Normal" and int(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


# Membuat multidimensional list
inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

# Input data PC
for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    inventaris.append([nama, status, ram])


# Evaluasi seluruh data PC
print("Hasil Evaluasi Inventaris:")

for pc in inventaris:
    nama = pc[0]
    status = pc[1]
    ram = pc[2]

    try:
        hasil = evaluasi(status, ram)

    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    # Menampilkan hasil menggunakan manipulasi string
    print('{ "PC": "' + nama +
          '", "Status": "' + hasil + '" }')