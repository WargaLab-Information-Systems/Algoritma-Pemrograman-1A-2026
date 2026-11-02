totalPenumpang = 0
totalPendapatan = []
jarak = []

while True:
    while True:
        try:
            inputJarak = float(input("Masukkan Jarak(km): "))
            print()
            break
        except ValueError:
            print("Value tidak valid!")
            continue

    if inputJarak == 0:
        break
    elif inputJarak < 0:
        print("Jarak tidak valid!")
        continue
    else:
        totalPenumpang += 1
        tarif = 3000 if inputJarak <= 5 else (3000 + (1000 * ((inputJarak - 5) // 1))) if inputJarak > 5 and inputJarak <= 15 else (13000 + (500 * ((inputJarak - 15) // 1)))

        if totalPenumpang % 5 == 0:
            tarif *= (50/100)
            print("Discounted")
            print()

        jarak.append(inputJarak)
        totalPendapatan.append(tarif)

print(f"Banyak penumpang: {totalPenumpang}")
print(f"Banyak pendapatan diperoleh: Rp{int(sum(totalPendapatan))}")
print(f"Jarak terjauh: {max(jarak):.1f}km")
print(f"Rata-rata jarak yang ditempuh {(sum(jarak) / len(jarak)):.2f}km")
print()
