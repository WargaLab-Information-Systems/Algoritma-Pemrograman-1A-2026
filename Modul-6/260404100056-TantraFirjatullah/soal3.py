def evaluasi_kondisi(status, ram):
    if status.lower() == "normal" and ram >= 8:
        return "Layak"
    return "Tidak Layak"

print()
inventaris = []
jumlah = int(input("Masukkan jumlah PC: "))
print()

for i in range(jumlah):
    print(f"Data PC ke-{i+1}")
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM(GB): ")

    inventaris.append([nama, status, ram])
    print()

print("Hasil Evaluasi:")
for baris in inventaris:
    nama, status, ram = baris[0], baris[1], baris[2]

    if ram.isdigit():
        ram = int(ram)

    try:
        hasil = evaluasi_kondisi(status, ram)
    except TypeError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + nama + '", "Status": "' + hasil + '" }')
