# Membuat fungsi palindrom
def cek_palindrom(kata):
    if kata == kata[::-1]:
        return True
    else: 
        return False

# Memasukkan kata
kata = input("Masukkan kata: ")

# Memanggil fungsi
hasil = cek_palindrom(kata)

# Menampilkan hasil 
if hasil == True:
    print(kata, "adalah palindrom")
else:
    print(kata, "bukan palindrom")