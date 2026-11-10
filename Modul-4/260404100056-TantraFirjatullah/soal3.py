besarPola = input("Masukkan Besar Pola: ")
while not(besarPola.isdigit()):
    print("Masukan tidak valid!")
    besarPola = input("Masukkan Besar Pola: ")

besarPola = int(besarPola)
cetakAngka = ""
cetakSpasi = ""
cetakAngkaReverse = ""

for i in range(1, besarPola + 1):
    cetakAngka += str(i % 10)
    cetakAngkaReverse = str(i % 10) + cetakAngkaReverse
    cetakSpasi = " " * 2 * (besarPola - i)

    print(cetakAngka, end="")
    print(cetakSpasi + " ", end="")
    print(cetakAngkaReverse, end="")
    print()
