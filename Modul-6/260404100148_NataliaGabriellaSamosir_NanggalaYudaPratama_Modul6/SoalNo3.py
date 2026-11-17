
print("=== SISTEM INVENTARIS PC LABORATORIUM ===")

# Meminta jumlah PC
jumlah_pc = int(input("Masukkan jumlah PC: "))

# Membuat list untuk menyimpan data PC
data_pc = []

# Input data setiap PC
for i in range(jumlah_pc):
    print("\nData PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status (Normal/Rusak): ")
    
    # Input RAM tanpa konversi tipe data
    ram = input("Masukkan kapasitas RAM (GB): ")

    # Menyimpan data dalam multidimensional list
    data_pc.append([nama, status, ram])


# Fungsi untuk mengevaluasi kelayakan PC
def evaluasi_pc(pc):
    if pc[1] == "Normal" and int(pc[2]) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


print("\n=== HASIL EVALUASI INVENTARIS PC ===")

# Melakukan evaluasi setiap PC
for pc in data_pc:
    try:
        hasil = evaluasi_pc(pc)

    except ValueError:
        hasil = "Format RAM Kacau"

    # Manipulasi string untuk mencetak hasil
    hasil_cetak = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'

    print(hasil_cetak)
