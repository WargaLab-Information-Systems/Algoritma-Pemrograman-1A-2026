def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    teks = input("Masukkan hari ke-N: ").strip()

    if teks == "":
        print("Input tidak boleh kosong!")
    elif not teks.isdigit():
        print("Input harus berupa bilangan bulat positif!")
    elif int(teks) <= 0:
        print("Bilangan harus lebih dari 0!")
    else:
        n = int(teks)
        break

hasil = fibonacci(n)

print(f"Jumlah pelanggan pada hari ke-{n} adalah {hasil} orang.")
