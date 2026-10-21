totalBelanja = int(input("Masukkan total belanjaan: Rp"))
if totalBelanja < 0:
    print("Total tidak valid, menolak untuk melanjutkan.")
    quit()

if (totalBelanja % 100000) == 0:
    totalBayar = 0
elif (totalBelanja % 50000) == 0:
    diskon1 = totalBelanja * (50/100)
    totalBayar = totalBelanja - diskon1
elif (totalBelanja % 10000) == 0:
    diskon1 = totalBelanja * (20/100)
    totalBayar = totalBelanja - diskon1
else:
    if totalBelanja >= 200000:
        diskon1 = totalBelanja * (10/100)
        totalBayar = totalBelanja - diskon1
    else:
        totalBayar = totalBelanja

status = "Poin Bertambah!" if totalBayar > 0 else "Tidak Ada Poin."

print()
print(f"Total sebelum diskon: {totalBelanja}")
print(f"Total: {totalBayar}")
print(status)
