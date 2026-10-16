# inputan suhu dan tekanan
suhu = float(input("masukkan suhu rektoar (°C):" ))
tekanan = float(input("masukkan tekanan gas (Bar): "))

print("nilai suhu :", suhu, "°C")
print("nilai tekanan:", tekanan, "Bar")

# pesan status bahaya sesuai kondisi
if suhu > 1000: 
    if tekanan > 50:
        status ="MELTDOWN! SEGERA EVAKUASI!"
    elif tekanan < 50:
        status ="bahaya suhu: segera turunkan daya!" 
elif suhu > 500:
    if tekanan > 30:
        status ="tekanan tidak stabil"
    else:
        status ="operasi reaktor normal"
else:
    status = "reaktor belum cukup panas"

print("hasil akhir dari status", status)

# operator tenary
pompa = "pompa maksimal" if suhu > 800 else "pompa normal"
print("Status pompa :", pompa)