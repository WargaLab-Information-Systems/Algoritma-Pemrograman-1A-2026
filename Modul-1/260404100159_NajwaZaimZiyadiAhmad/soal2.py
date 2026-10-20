# Program Menghitung Volume Kerucut

print("=== PROGRAM MENGHITUNG VOLUME KERUCUT ===")

# Input jari-jari dan tinggi
jari_jari = float(input("Masukkan jari-jari kerucut (cm): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))

# Nilai phi
phi = 3.14

# Menghitung volume kerucut
volume = (1/3) * phi * jari_jari * jari_jari * tinggi

# Menampilkan hasil
print("\n=== HASIL PERHITUNGAN ===")
print(f"Jari-jari kerucut : {jari_jari} cm")
print(f"Tinggi kerucut   : {tinggi} cm")
print(f"Volume kerucut   : {volume:.2f} cm³")