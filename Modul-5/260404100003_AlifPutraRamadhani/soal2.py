# Mendefinisikan fungsi pengecek palindrom
def cek_palindrom(kata):
    kata_dibalik = ""
    for karakter in kata:
        kata_dibalik = karakter + kata_dibalik 

    if kata == kata_dibalik:
        return True
    else:
        return False

while True:
    input_kata = input("Masukkan sebuah kata: ")
    if not input_kata:
        print("Masukan Tidak Boleh Kosong")
        print()
        continue
        
    if input_kata[0] == "-":
        print("Masukan Tidak Boleh Minus")
        print()
        continue

    ada_angka = False
    for karakter in input_kata:
        if karakter >= '0' and karakter <= '9':
            ada_angka = True
            break 
            
    if ada_angka == True:
        print("Masukan Tidak Boleh Mengandung Angka")
        print()
        continue
    else:
        break

hasil = cek_palindrom(input_kata)

if hasil == True:
    print("Kata", input_kata, "merupakan palindrom.")
else:
    print("Kata", input_kata, "bukan merupakan palindrom.")