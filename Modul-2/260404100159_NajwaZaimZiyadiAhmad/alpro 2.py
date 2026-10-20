total_belanjaan = int(input("masukkan nilai: "))

if total_belanjaan % 100000 == 0:
    diskon = 100
    total_akhir = 0
elif total_belanjaan % 50000 == 0:
    diskon = 50
    total_akhir = total_belanjaan - total_belanjaan * 50 // 100
elif total_belanjaan % 10000 == 0:
    diskon = 20
    total_akhir = total_belanjaan - total_belanjaan * 20 // 100
elif total_belanjaan >= 200000:
    diskon = 10
    total_akhir = total_belanjaan - total_belanjaan * 20 // 100
else:
    diskon = 0
    total_akhir = total_belanjaan

point = "Poin bertambah" if total_akhir > 0 else "Tidak Ada poin"

print("total awal: ",total_belanjaan)
print("total setelah diskon: ",total_akhir)
print("jumlah diskon: ",diskon)
print( "Status point: ", point)
