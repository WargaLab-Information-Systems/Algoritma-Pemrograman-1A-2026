jari_jari = float(input("Masukkan jari-jari alas kerucut (cm): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))

volume = (1 / 3) * 22/7 * (jari_jari ** 2) * tinggi

print(f"Volume kerucut dengan jari-jari {jari_jari} cm dan tinggi {tinggi} cm")
print(f"adalah {volume} cm^3")