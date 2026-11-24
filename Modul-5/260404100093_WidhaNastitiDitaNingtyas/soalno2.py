def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False


kata = input("Masukkan sebuah kata: ")

hasil = palindrom(kata)

if hasil == True:
    print(kata, "merupakan kata palindrom")
else:
    print(kata[::-1])
    print(kata, "bukan merupakan kata palindrom")