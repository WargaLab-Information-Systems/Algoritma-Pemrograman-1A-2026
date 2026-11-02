def fibonacci(h):
    if h <= 1:
        return h
    return fibonacci(h - 1) + fibonacci(h - 2)

hari = input("Masukkan hari yang ingin dilihat: ")
while not hari.isdigit():
    print("Masukan tidak valid")
    hari = input("Masukkan hari yang ingin dilihat: ")
hari = int(hari)

print(f"Jumlah Pelanggan pada hari itu adalah {fibonacci(hari)}")

for i in range(1, hari + 1):
    print(fibonacci(i), end=" ")
