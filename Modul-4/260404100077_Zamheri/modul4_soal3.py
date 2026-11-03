n = input("Masukkan ukuran pola: ")

while n.isdigit() == False:
    print("Masukan tidak benar!")
    n = input("Masukkan ukuran pola: ")

n = int(n)


for baris in range(1, n + 1):

    
    for a in range(1, baris + 1):
        print(a % 10, end="")


    for s in range(2 * (n - baris) + 1):
        print(" ", end="")


    for b in range(baris, 0, -1):
        print(b % 10, end="")

   
    print()
