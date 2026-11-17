print("=== PROGRAM CEK PALINDROM ===")

# Membuat fungsi palindrom
def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

# Input kata dari pengguna
kata = input("Masukkan sebuah kata: ")

# Memanggil fungsi
hasil = palindrom(kata)

# Menampilkan hasil
if hasil == True:
    print("Kata", kata, "merupakan PALINDROM")
else:
    print("Kata", kata, "BUKAN PALINDROM")
