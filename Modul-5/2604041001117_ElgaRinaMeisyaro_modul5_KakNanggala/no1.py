# Membuat fungsi
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Input hari
hari = int(input("Masukkan hari ke-: "))

# Memanggil fungsi
hasil = fibonacci(hari)

# Menampilkan hasil 
print("Jumlah pelanggan:", hasil)