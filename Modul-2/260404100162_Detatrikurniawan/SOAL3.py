suhu = float(input("Masukkan suhu reaktor (Celsius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("\nDATA REAKTOR")
print(f"Suhu    : {suhu} Celsius")
print(f"Tekanan : {tekanan} Bar")

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

print(f"Status  : {status}")

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print(f"Pompa   : {status_pompa}")