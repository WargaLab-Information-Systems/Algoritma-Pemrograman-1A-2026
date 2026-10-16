while True:
    nilai = input("Masukkan n (2-15): ")
    if nilai.strip() == "":
        print("Input tidak boleh kosong!")
        continue
    if not nilai.lstrip("-").isdigit():
        print("Hanya boleh angka!")
        continue
    n = int(nilai)
    if n < 0:
        print("Tidak boleh negatif, ulangi!")
    elif n < 2 or n > 15:
        print("n tidak valid, ulangi!")
    else:
        break

for k in range(1, 2 * n):
    if k <= n:
        i = k
    else:
        i = 2 * n - k

    baris = " " * (n - i)

    for j in range(1, i + 1):
        baris += str(j % 10)
    for j in range(i - 1, 0, -1):
        baris += str(j % 10)

    print(baris)