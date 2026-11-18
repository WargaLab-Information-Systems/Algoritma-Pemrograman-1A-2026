# Mendefinisikan Fungsi Rekursif (Deret Fibonacci)
def hitung_pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return hitung_pelanggan(n - 1) + hitung_pelanggan(n - 2)

while True:
    input_hari = input("Masukkan hari ke-N: ")
    if not input_hari:
        print("Masukan Tidak Boleh Kosong")
        print()
        continue        
    if input_hari[0] == "-":
        print("Masukan Tidak Boleh Minus")
        print()
        continue
    hari_int = True
    for karakter in input_hari:
        if karakter < '0' or karakter > '9':
            hari_int = False
            break 
            
    if not hari_int:
        print("Masukan Tidak Boleh Selain Angka")
        print()
        continue

    hari = int(input_hari)
    if hari == 0:
        print("Masukan Tidak Boleh Nol")
        print()
        continue
    else:
        break 

jumlah = hitung_pelanggan(hari)
print("Jumlah pelanggan Bu Lastri pada hari ke-", hari, "adalah:", jumlah, "orang")