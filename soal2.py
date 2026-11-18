def cek_palindrom(kata):
    terbalik = ""
    for huruf in kata:
        terbalik = huruf + terbalik
    return kata == terbalik

kata = input("Masukkan kata: ")
hasil = cek_palindrom(kata)
print("Hasil fungsi:", hasil)

if hasil:
    print(kata, "adalah palindrom")
else:
    print(kata, "bukan palindrom")