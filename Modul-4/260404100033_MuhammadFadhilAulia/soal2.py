totalGaji = 0

for i in range(1, 8):
    print("==== HARI KE - ", i, " ====")
    while True:
        lembur = input("Masukkan Jumlah Lembur Karyawan(Jumlah Jam)= ")
        huruf = lembur != ""
        for karakter in lembur:
            if karakter < "0" or karakter > "9":
                huruf = False
        if huruf == True:
            lembur = int(lembur)
            break
        print("Dilarang memasukkan input Angka Minus(-), Input Yang selain di suruh, (Contoh Yang Benar -----> 3)")

    while True:
        malam = input("Masukkan Jumlah Shift Malam(Bentuk Jumlah Hari)= ")
        huruf = malam != ""
        for karakter in malam:
            if karakter < "0" or karakter > "9":
                huruf = False
        if huruf == True:
            malam = int(malam)
            break
        print("Dilarang memasukkan input Angka Minus(-), Input Yang selain di suruh, (Contoh Yang Benar -----> 3)")

    # for i in range(1, 8):
    gaji = 100000
    if lembur == 0:
        gaji += 0
    elif lembur >= 1 and lembur <= 3:
        for jam in range(1, lembur + 1):    
            gaji += lembur * 25000
    elif lembur <= 4:
        gaji += 100000
    elif lembur <= 6 or lembur == 5:
        gaji += 200000
    elif lembur == 8 or lembur == 7:
        gaji += 300000
    else:
        print("\n==== Jumlah Lembur Melebihi Batas ====")

    if malam == 1:
        gaji += 50000

    totalGaji += gaji

print("\n==== Total Gaji Karyawan = ", totalGaji, " ====")