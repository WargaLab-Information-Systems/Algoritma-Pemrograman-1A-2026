#  program pemeriksaan lampu
while True:
    baris_str = input("Masukkan jumlah baris: ")
    if not baris_str:
        print("Masukan Tidak Boleh Kosong")
        continue
    if baris_str[0] == "-":
        print("Masukan Tidak Boleh Minus")
        continue
    baris_int = True
    for karakter in baris_str:
        if karakter not in '0987654321':
            baris_int = False
            break
    if not baris_int:
        print("Masukan Tidak Boleh Selain Angka")
        continue
    baris = int(baris_str)
    if baris <= 0:
        print("Angka Tidak Boleh Minus dan 0")
        continue
    else:
        break

while True:
    lampu_str = input("Masukkan jumlah lampu tiap baris: ")
    if not lampu_str:
        print("Masukan Tidak Boleh Kosong")
        continue
    if lampu_str[0] == "-":
        print("Masukan Tidak Boleh Minus")
        continue
    lampu_int = True
    for karakter in lampu_str:
        if karakter not in '0987654321':
            lampu_int = False
            break
    if not lampu_int:
        print("Masukan Tidak Boleh Selain Angka")
        continue
    lampu = int(lampu_str)
    if lampu == 0:
        print("Angka Tidak Boleh 0")
        continue
    else:
        break

for n in range(1, baris + 1):
    print("Nomor Lampu", n)
    for m in range(1, lampu + 1):
        if m % 3 == 0:
            print("lampu",m,"gangguan")
        else:
            print("lampu",m,"aktif")

print("Jangan Lupa Periksa Sumber Daya Lampu Taman")