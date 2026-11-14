def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
hari = int(input("masukkan hari ke-N: "))

if hari > 0:
    print("jumlah pelanggan hari ke-", hari, "adalah:", fibonacci(hari))
else:
    print("masukkan bilangan positif!")