def outputHasil():
    print("Nama-Nama Panitia:")
    for i in range(len(panitia)):
        print(f"{i+1}. {panitia[i]}")

def masukkan_nama():
    panitia = []
    print()
    print("Ketik 'selesai' untuk memproses.")
    while True:
        data = input("Masukkan Nama: ")
        if data.lower() == "selesai":
            break
        panitia.append(data)
    return panitia

panitia = masukkan_nama()

valid = []
for nama in panitia:
    if nama.lower() == "admin" or len(nama) < 4:
        print(f'Nama ini "{nama}" tidak valid! Nama dihapus.')
    else:
        valid.append(nama)
panitia = valid

print()
while True:
    penyusup = input("Masukkan Nama Penyusup: ")
    if penyusup in panitia:
        panitia.remove(penyusup)
        print("Penyusup sudah dihapus.")
        print()
        break
    else:
        print("Nama penyusup tidak ditemukan.")
        continue

outputHasil()
