def input_hari():
    while True:
        n = input("Masukkan hari ke-N: ")
        if n.strip() == "":
            print("Input tidak boleh kosong!")
        elif n.startswith("-") and n[1:].isdigit():
            print("Angka tidak boleh negatif!")
        elif not n.isdigit():
            print("inputan kamu bukan tipe data yang diminta!")
        elif int(n) <= 0:
            print("Angka harus lebih besar dari 0!")
        else:
            return int(n)

def pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pelanggan(n - 1) + pelanggan(n - 2)

N = input_hari()
hasil = pelanggan(N)
print("Jumlah pelanggan pada hari ke", N, "adalah", hasil, "orang")
