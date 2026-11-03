def palindrom(kata):
    panjang = len(kata)
    for i in range(panjang):
        if kata[i] != kata[panjang - 1 - i]:
            return False
    return True

while True:
    kata = input("Masukkan sebuah kata: ")
    if kata.strip() == "":
        print("Input tidak boleh kosong!")
    elif kata.lstrip("-").isdigit():
        print("Tolong jangan input angka postif maupun negatif, yang diminta di sini teks/kata!")
    elif kata.startswith("-"):
        print("Tanda minus tidak boleh, yang diminta di sini teks/kata saja ya mas!")
    else:
        break

hasil = palindrom(kata)

print("Hasil:", hasil)
if hasil == True:
    print(kata, "adalah palindrom")
else:
    print(kata, "bukan palindrom")