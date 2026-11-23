# Membuat fungsi untuk memeriksa kata palindrom
def palindrom(kata):

    # Membalik kata yang dimasukkan
    balik = kata[::-1]

    # Memeriksa apakah kata asli sama dengan kata yang dibalik
    if kata == balik:
        return True
    else:
        return False


# Meminta pengguna memasukkan sebuah kata
kata = input("Masukkan kata: ")

# Memanggil fungsi palindrom
hasil = palindrom(kata)

# Menampilkan hasil pemeriksaan
if hasil == True:
    print(kata, "adalah kata palindrom")
else:
    print(kata, "bukan kata palindrom")
