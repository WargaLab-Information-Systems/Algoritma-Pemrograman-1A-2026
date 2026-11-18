def evaluasi_pc(status, ram):
    ram = int(ram)
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

inventaris = []
jumlah = int(input("Jumlah PC: "))

for i in range(jumlah):
    nama = input("Nama PC: ")
    status = input("Status PC (Normal/Rusak): ")
    ram = input("Kapasitas RAM: ")
    inventaris.append([nama, status, ram])

for data in inventaris:
    hasil = evaluasi_pc(data[1], data[2])
    print('{"PC": "' + data[0] + '", "Status": "' + hasil + '"}')