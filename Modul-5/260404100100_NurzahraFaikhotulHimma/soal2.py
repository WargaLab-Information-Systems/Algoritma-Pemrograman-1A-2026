def palindrom(kata):

    if kata == kata[::-1]:
        return True
    else:
        return False


teks = input("Masukkan sebuah kata: ")
hasil = palindrom(teks)

if hasil == True:
    print(teks, "merupakan kata palindrom")
else:
    print(teks, "bukan merupakan kata palindrom")