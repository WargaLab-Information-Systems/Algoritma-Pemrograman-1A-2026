print("=== PROGRAM JUMLAH PELANGGAN BU LASTRI ===")

# Membuat fungsi rekursif
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Memasukkan hari
hari = int(input("Masukkan hari ke-N: "))

# Menampilkan hasil
hasil = fibonacci(hari)

print("Jumlah pelanggan pada hari ke-", hari, "adalah:", hasil, "orang")
