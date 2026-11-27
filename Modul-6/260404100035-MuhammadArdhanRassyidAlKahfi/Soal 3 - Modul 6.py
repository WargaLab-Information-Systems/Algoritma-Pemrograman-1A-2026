def evaluasi_pc(pc):
    ram = float(pc[2])

    if ram >= 8 and pc[1] == "Normal":
        return "Layak"
    else:
        return "Tidak Layak"


while True:
    try:
        jumlah = input("Masukkan jumlah PC: ").strip()

        if jumlah == "":
            print("Peringatan: Jumlah PC tidak boleh kosong!")
            continue

        jumlah = int(jumlah)

        if jumlah <= 0:
            print("Peringatan: Jumlah PC harus lebih dari 0!")
            continue

        break

    except ValueError:
        print("Peringatan: Jumlah PC harus berupa angka bulat!")

inventaris = []

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    while True:
        nama_pc = input("Masukkan nama PC: ").strip()

        if nama_pc == "":
            print("Peringatan: Nama PC tidak boleh kosong!")
        else:
            break

    while True:
        status = input("Masukkan status (Normal/Rusak): ").strip()

        if status.lower() == "normal":
            status = "Normal"
            break
        elif status.lower() == "rusak":
            status = "Rusak"
            break
        else:
            print("Peringatan: Status harus Normal atau Rusak!")

    ram = input("Masukkan kapasitas RAM (GB): ")

    inventaris.append([nama_pc, status, ram])

print("\nHasil Evaluasi Inventaris PC:")

for pc in inventaris:
    try:
        hasil = evaluasi_pc(pc)
    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')