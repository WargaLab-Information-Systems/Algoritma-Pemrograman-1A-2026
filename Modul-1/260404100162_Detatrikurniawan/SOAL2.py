jari_jari = float(input("Masukkan jari-jari alas kerucut (cm): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))

pi = 22/7
volume = (1/3) * pi * jari_jari**2 * tinggi

print(f"Volume kerucut = {volume:.2f} cm^3")