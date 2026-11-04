def n(x):
    if x == 1 or x == 2:
        return 1
    return n(x-1) + n(x-2)

while True:    
    x = int(input("Masukkan Hari Ke : "))
    huruf = x != ""
    for karakter in x:
        if karakter < "0" or karakter > "9":
            huruf = False
    if huruf == True:
        break
    print("Maaf, Yang Anda Inputkan Itu Salah(Contoh : 1, 2, 3)")
    
hari = 1
a, b = 1, 1

for hari in range(1, x + 1):
    print(f"Hari ke-{hari} ==> {n(hari)} Orang")
    a, b = b, a + b
    hari += 1

print(f"\nJumlah Pelanggan Kue Bu Lestari pada Hari ke- {x} ==> {n(x)} Orang")