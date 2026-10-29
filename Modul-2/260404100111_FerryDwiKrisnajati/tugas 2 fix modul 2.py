#Diskon KOPERASI NDESO
total_belanja = int(input("Masukkan total belanja:Rp"))
#menentukan diskon
if total_belanja % 100000 == 0:
    diskon = total_belanja
elif total_belanja % 50000 == 0:
    diskon = total_belanja*50 /100
elif total_belanja % 10000 ==0:
    diskon = total_belanja*20/100
elif total_belanja >= 200000:
    diskon = total_belanja*10/100
else:
    diskon = 0
#menghitung total baya
total_bayar = total_belanja-diskon
#ternary
status_poin = "poin bertambah" if total_bayar > 0 else "tidak ada poin" 
print ("===HASIL BELANJA===")
print ("Total belanja awal : rp",total_belanja)
print ("Diskon : Rp",diskon)
print ("Total yang dibayar : Rp",total_bayar)
print ("Status poin :", status_poin)