
# Program Pemantauan Reaktor Nuklir Chernobyl

# Input suhu dan tekanan
suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# Menampilkan suhu dan tekanan
print("\n=== DATA PEMANTAUAN REAKTOR ===")
print("Suhu reaktor:", suhu, "°C")
print("Tekanan gas:", tekanan, "Bar")

# Menentukan status bahaya reaktor
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

# Menentukan status pompa menggunakan ternary operator
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# Menampilkan hasil pemantauan
print("\n=== HASIL PEMANTAUAN ===")
print("Status Bahaya:", status)
print("Status Pompa:", pompa)
