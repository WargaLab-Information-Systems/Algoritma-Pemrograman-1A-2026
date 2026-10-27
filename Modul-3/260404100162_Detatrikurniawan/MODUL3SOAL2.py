while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))
    if 2 <= n <= 15:
        break
    print("Input tidak valid, ulangi!")

for i in range(1, 2 * n):
    if i <= n:
        baris = i
    else:
        baris = 2 * n - i

    teks = " " * (n - baris)

    for j in range(1, baris + 1):        
        teks += str(j % 10)
    for j in range(baris - 1, 0, -1):   
        teks += str(j % 10)

    print(teks)