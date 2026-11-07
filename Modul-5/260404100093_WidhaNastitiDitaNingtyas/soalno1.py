def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Masukkan hari ke-: "))

for i in range (1, n, n-1):
    print(i)

while n <= 0:
    print("Input harus bilangan bulat positif!")
    n = int(input("Masukkan hari ke-: "))

hasil = fibonacci(n)

print("Jumlah pelanggan pada hari ke-", n, "adalah:", hasil)