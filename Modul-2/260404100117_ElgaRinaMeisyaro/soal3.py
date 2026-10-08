suhu = float(input("Masukkan suhu: "))
tekanan = float(input("Masukkan tekanan: "))

print("=================================================")

print("Suhu:", suhu)
print("Tekanan:", tekanan)

if suhu > 1000:
    if tekanan > 50: 
        print("MELTDOWN: SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu > 500:
    if tekanan > 30:
        print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print(pompa)

print("================================================")
