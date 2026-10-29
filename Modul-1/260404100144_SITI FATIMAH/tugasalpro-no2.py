r=7
t=12

r = float(input("Masukkan jari-jari kerucut (cm): "))
t = float(input("Masukkan tinggi kerucut (cm): "))

phi = 3.14

volume = (1/3) * phi * r * r * t

print("Jari-jari :", r, "cm")
print("Tinggi    :", t, "cm")
print("Volume    :", volume, "cm³")