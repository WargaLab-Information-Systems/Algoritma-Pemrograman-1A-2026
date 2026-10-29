# Meminta pengguna masukkan ukuran pola
n = int(input("Masukkan bilangan bulat positif"))

# Mengatur jumlah baris pola dari 1 sampai n
for i in range (1, n + 1):
    # Membuat piramida pertama dengan angka yang bertambah
    for angka in range(1, i + 1):
        print(angka, end=" ")

    #Mengatur jarak antara piramida pertama dan kedua
    for spasi in range (2 * (n- i) + 1):
        print(" ", end=" ")

    #Mencetak piramida kedua dengan angka yang menurun 
    for angka in range (i, 0, -1):
        print(angka, end= " ")

    # Berpindah ke baris baru setelah kedua pola selesai dicetak
    print ()

