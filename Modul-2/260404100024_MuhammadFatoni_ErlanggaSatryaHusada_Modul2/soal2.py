total_belanja = input("Masukkan total belanja: ").strip()

if total_belanja == "":
    print("Total belanja tidak boleh kosong.")
elif total_belanja < 0:
    print("Total belanja tidak boleh negatif.")
elif not total_belanja.isdigit():
    print("Total belanja harus berupa angka.")
else:
    total_belanja = int(total_belanja)

    if total_belanja == 0:
        print("Total belanja harus lebih dari 0.")
    else:
        if total_belanja % 100000 == 0:
            diskon = 100
        elif total_belanja % 50000 == 0:
            diskon = 50
        elif total_belanja % 10000 == 0:
            diskon = 20
        elif total_belanja >= 200000:
            diskon = 10
        else:
            diskon = 0

        bayar = total_belanja - total_belanja * diskon // 100
        poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"

        print("Total belanja awal:", total_belanja)
        print("Diskon:", diskon, "%")
        print("Total bayar:", bayar)
        print("Status poin:", poin)