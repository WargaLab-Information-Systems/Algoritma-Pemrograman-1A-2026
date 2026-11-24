def evaluasi_pc(status, ram):
    if status.lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


pc = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status PC (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    pc.append([nama, status, ram])


print("\nHasil Evaluasi PC:")

for data in pc:
    try:
        kelayakan = evaluasi_pc(data[1], data[2])

    except TypeError:
        kelayakan = "Format RAM Kacau"

    hasil = '{ "PC": "' + data[0] + '", "Status": "' + kelayakan + '" }'

    print(hasil)