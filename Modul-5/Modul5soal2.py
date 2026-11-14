def palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("Masukkan kata: ")
hasil = palindrom(kata)

if hasil:
    print("Kata ini adalah palindrom.")
else:
    print("Kata ini bukan palindrom.")