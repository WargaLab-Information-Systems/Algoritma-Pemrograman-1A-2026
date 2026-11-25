def baris(baris, kolom):
    for b in range(1, baris+1):
        for k in range(1, kolom+1):
            cetak = str(b % 10)
            print(cetak, end=" ")
        print()
    print()

a = 1
while True:
    try:
        b = int(input("Masukkan password: "))
    except ValueError as errorCatch:
        print(f"error adalah: {errorCatch}")
        print("Harus berupa angka!")
        continue
    if b != 5:
        print("Password Salah")
        continue
    break

if a == 1 and b == 5:
    baris(int(input("Masukkan baris: ")), int(input("Masukkan kolom: ")))
else:
    print("password salah")
