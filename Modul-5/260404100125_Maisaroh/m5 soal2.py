def cekPalindrom(kata):

    if kata == kata[::-1]:
        return True
    else:
        return False

teks = input("masukkan sebuah kata: ")

if cekPalindrom(teks):
    print("kata tersebut adalah palindrom")
else:
    print("kata tersebut bukan palindrom")