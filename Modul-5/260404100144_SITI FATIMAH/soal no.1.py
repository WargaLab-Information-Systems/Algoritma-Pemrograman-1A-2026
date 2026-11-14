# Membuat fungsi untuk menghitung jumlah pelanggan
def fibonacci(n):

    # Jika hari pertama atau kedua, jumlah pelanggan adalah 1
    if n == 1 or n == 2:
        return 1

    # Menghitung jumlah pelanggan dari dua hari sebelumnya
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

hari = int(input("Masukkan hari ke-N: "))

# Memeriksa apakah hari yang dimasukkan merupakan bilangan positif
if hari > 0:

    # Memanggil fungsi fibonacci untuk menghitung jumlah pelanggan
    hasil = fibonacci(hari)

    # Menampilkan jumlah pelanggan pada hari tersebut
    print("Jumlah pelanggan pada hari ke-", hari, "adalah", hasil)

# Jika pengguna memasukkan angka 0 atau negatif
else:
    print("Masukkan bilangan bulat positif!")
