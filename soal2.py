n = int(input("Tinggi setengah menara (2-15): "))
while n < 2 or n > 15:
    print("Harus 2 sampai 15!")
    n = int(input("Tinggi setengah menara (2-15): "))

for baris in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
    teks = ""
    for i in range(1, baris + 1):
        teks = teks + str(i % 10)
    for i in range(baris - 1, 0, -1):
        teks = teks + str(i % 10)
    print(" " * (n - baris) + teks)