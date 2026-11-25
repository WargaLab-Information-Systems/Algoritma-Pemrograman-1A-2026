while True:
    n = int(input())
    if n < 2 or n > 15:
        continue
    else:
        break
print()
for i in range(1, 2 * n):
    if i <= n:
        baris = i
    else:
        baris = 2 * n - i

    cetak = " " * (n - baris)

    for x in range(1, baris + 1):
        cetak += str(x % 10)

    for x in range(baris - 1, 0, -1):
        cetak += str(x % 10)

    print(cetak)
