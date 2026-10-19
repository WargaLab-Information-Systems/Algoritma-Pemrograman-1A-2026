while True:
    suhu = input("masukkan suhu reaktor (c) :")

    if suhu == "" or suhu.isspace():
        print("Input tidak boleh kosong! Silakan masukkan angka.")
        continue
    try :
        suhu = float(suhu)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar (bukan huruf).")
        continue
    if suhu < 0 :
        print("maaf tidak boleh memasukkan angka negatif, silahkan input ulang")
        continue
    break
while True:
    tekanan = input("masukkan tekanan gas (bar) :")

    if tekanan == "" or tekanan.isspace():
        print("input tidak boleh kosong! Silahkan masukkan angka")
        continue
    try :
        tekanan = float(tekanan)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar (bukan huruf).")
        continue 
    if tekanan < 0 :
            print("maaf tidak boleh memasukkan angka negatif, silahkan input ulang")
            continue
    break

if suhu > 1000 :
    if tekanan > 50 :
        status = "MELTDOWN! SEGERA DI EVAKUASI"
    else :
        status = "suhu berbahaya : segera turunkan daya!"
elif suhu > 500 :
    if tekanan >30 :
        status = "tekanan anda tidak stabil"
    else :
        status = "operasi reaktor normal"
else :
    status = "reaktor belum cukup panas"

# operator ternary
pompa = "pompa maksimal" if suhu > 800 else "pompa normal"
print("\n--- RINCIAN KONDISI REAKTOR ---")
print("suhu tubuh anda    :", suhu, "c")
print("tekanan tubuh anda :", tekanan, "bar")
print("status             :", status)
print("pompa              :", pompa)