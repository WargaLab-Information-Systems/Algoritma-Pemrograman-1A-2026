while True:
    baris = input("Masukin jumlah baris lampu: ")
    if baris == "":
        print("Input tidak boleh kosong!")
    elif baris.startswith("-") and baris[1:].isdigit():
        print("Angka tidak boleh negatif!")
    elif not baris.isdigit():
        print("Input harus berupa angka!")
    elif int(baris) <= 0:
        print("Angka harus lebih besar dari 0!")
    elif int(baris) > 9:
        print("Angka tidak boleh lebih dari 9!")
    else:
        baris = int(baris)
        break

while True:
    lampu = input("Masukin jumlah lampu pada setiap baris: ")
    if lampu == "":
        print("Input tidak boleh kosong!")
    elif lampu.startswith("-") and lampu[1:].isdigit():
        print("Angka tidak boleh negatif!")
    elif not lampu.isdigit():
        print("Input harus berupa angka!")
    elif int(lampu) <= 0:
        print("Angka harus lebih besar dari 0!")
    elif int(lampu) > 9:
        print("Angka tidak boleh lebih dari 9!")
    else:
        lampu = int(lampu)
        break

for b in range(1, baris + 1):
    print("Baris", b)
    for l in range(1, lampu + 1):
        if l % 3 == 0:
            print("Lampunya", l, ": gangguan")
        else:
            print("Lampunya", l, ": Berfungsi normal")

print("Periksaan selesai. Silakan periksa sumber listrik utama taman.")