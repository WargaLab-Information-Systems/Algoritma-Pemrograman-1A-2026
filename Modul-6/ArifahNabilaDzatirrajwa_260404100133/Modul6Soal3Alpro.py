def evaluasi_pc(pc):
    ram = int(pc[2])
    if pc[1] == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"
    
data_pc = []

jumlah = int(input("Masukkan jumlah PC: "))
for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status PC: ")
    ram = input("Kapasitas RAM (GB): ")
    data_pc.append([nama, status, ram])

print("Hasil Evaluasi Inventaris PC:")

for pc in data_pc:
    try:
        kelayakan = evaluasi_pc(pc)
    except ValueError:
        kelayakan = "Format RAM Kacau"

    print("PC: " + pc[0] + ", Status: " + kelayakan)