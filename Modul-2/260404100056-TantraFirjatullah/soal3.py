suhu = float(input("Masukkan suhu: "))
tekanan = int(input("Masukkan tekanan: "))

suhuC = suhu
suhuF = (suhuC * 1.8) + 32
suhuR = suhuC / 1.25

if suhuC > 1000:
    if tekanan > 50:
        statusReaktor = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        statusReaktor = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhuC > 500:
    if tekanan > 30:
        statusReaktor = "Tekanan tidak stabil!"
    else:
        statusReaktor = "Operasi reaktor normal."
else:
    statusReaktor = "Reaktor tidak cukup panas!"

statusPompa = "Pompa Maksimal" if suhuC > 800 else "Pompa Normal"

print()
print(f"Suhu berada pada {suhuC}°C dan Tekanan pada {tekanan} Bar")
print(f"Suhu berada pada {suhuF}°F")
print(f"Suhu berada pada {suhuR}°Re")
print(statusReaktor)
print(statusPompa)
