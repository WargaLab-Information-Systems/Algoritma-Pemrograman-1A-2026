# Program Menghitung Volume Kerucut

# Input
r = float(input("Masukkan jari-jari alas (cm):"))
t = float(input("Masukkan tinggi kerucut (cm):"))

# Menghitung Volume Kerucut
phi = 22 / 7
volume = (1 / 3) * phi * r**2 * t

# Output
print("\n Hasil Perhitungan Volume Kerucut")
print("Jari-jari alas =", r, "cm")
print("Tinggi kerucut =", t, "cm")
print("Volume kerucut =", volume, "cm³")