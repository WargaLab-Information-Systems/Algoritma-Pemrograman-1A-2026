def palindrom(kata):
    kata = kata.lower()

    if kata == kata[::-1]:
        return True
    else:
        return False


while True:
    teks = input("Masukkan sebuah kata: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isalpha():
        print("Input harus berupa huruf, bukan angka atau simbol!")
    else:
        break

hasil = palindrom(teks)

if hasil == True:
    print(f"Kata '{teks}' merupakan palindrom.")
else:
    print(f"Kata '{teks}' bukan merupakan palindrom.")