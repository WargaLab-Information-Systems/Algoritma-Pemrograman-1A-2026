# Program Dua Piramida Angka Berhadapan - Bima

n = int(input("Masukkan bilangan bulat positif n: "))
jarak = 3  # jarak minimal antar pola (pada baris terakhir)

for i in range(1, n + 1):
    # Pola kiri: angka naik 1 sampai i
    for j in range(1, i + 1):
        print(j, end="")

    # Spasi pemisah: makin kecil ke bawah, minimal sebesar jarak
    for s in range((n - i) * 2 + jarak):
        print(" ", end="")

    # Pola kanan (cerminan): angka turun i sampai 1
    for k in range(i, 0, -1):
        print(k, end="")

    print()  # pindah baris