def cek_palindrome(kata):
    terbalik = ""
    for karakter in kata:
        terbalik = karakter + terbalik
    return kata == terbalik

while True:
    kata = input("Masukkan kata : ")
    huruf = kata != ""
    for karakter in kata:
        if huruf == False:
            break
    if huruf == True:
        break
    print("Maaf, Yang Anda Inputkan Itu Kosong")

if cek_palindrome(kata):
    print(f"hasil : {cek_palindrome(kata)}")
    print(f"Huruf {kata} adalah PALINDROME")
else:
    print(f"hasil : {cek_palindrome(kata)}")
    print(f"Huruf {kata} adalah BUKAN PALINDROME")