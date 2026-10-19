# Perhitungan Suhu dan Tekanan

while True:
    isi = input("Masukkan suhu: ")
    if isi == "":
        print("Peringatan: Input tidak boleh kosong!")
    else:
        try:
            suhu = float(isi)
            break
        except ValueError:
            print("Peringatan: Tidak boleh memasukkan karakter selain bilangan bulat atau desimal!")

while True:
    isi = input("Masukkan tekanan: ")
    if isi == "":
        print("Peringatan: Input tidak boleh kosong!")
    else:
        try:
            tekanan = float(isi)
            break
        except ValueError:
            print("Peringatan: Tidak boleh memasukkan karakter selain bilangan bulat atau desimal!")

print("Suhu:", suhu)
print("Tekanan:", tekanan)

if suhu > 1000:
    if tekanan > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu > 500:
    if tekanan > 30:
        print("Tekanan Tidak Stabil")
    else:
        print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print(pompa)