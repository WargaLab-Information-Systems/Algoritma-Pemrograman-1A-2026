
suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

if suhu > 1000:
    if tekanan > 50:
        statusBahaya = "MELTDOWN! SEGERA EVAKUASI!"
    else:
     statusBahaya = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        statusBahaya = "Tekanan Tidak Stabil"
    else:
        statusBahaya = "Operasi Reaktor Normal"
else:
    statusBahaya = "Reaktor Belum Cukup Panas"

statusPompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# Output hasil
print("\n--- LAPORAN STATUS REAKTOR ---")
print("Suhu Reaktor:", suhu, "°C")
print("Tekanan Gas:", tekanan, "Bar")
print("Status Bahaya:", statusBahaya)
print("Status Pompa:", statusPompa)