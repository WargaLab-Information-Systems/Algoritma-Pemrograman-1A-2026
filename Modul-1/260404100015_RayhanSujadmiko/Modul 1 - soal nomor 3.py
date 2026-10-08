#SOAL NOMOR 2 DALAM MODUL 1 PRAKTIKUM
#MENGHITUNG KEBUTUHAN BAHAN BAKAR DIMAS

#Data yang diambil dari soal
print("Diketahui Dimas berencana silahturahmi ke rumah keluarganya yang berada di luar kota")
print("Jarak kerumah keluarga Dimas 100km, Dimas memutuskan pulang pada hari yang sama")
print("Konsumsi bahan bakar motor dimas sebesar 1 liter untuk 40km")
print("Sebelum berangkat mendapati ada sisa 1,5 liter bahan bakar didalam tangkinya")
print("harga bahan bakar di SPBU sebesar Rp10.000/liter")

#Data yang diketahui
jarak_pergi = 100 #KM
jarak_untuk_1liter = 40 #KM
sisa_bbm = 1.5 #Liter
harga_bensin_1liter = 10000 #Rp

#Perhitungan
total_jarak = jarak_pergi * 2
kebutuhan_bbm = total_jarak / jarak_untuk_1liter
total_bbm = kebutuhan_bbm - sisa_bbm
total_biaya = total_bbm * harga_bensin_1liter

#Output
print("Total jarak yang harus ditempuh Dimas =", total_jarak,"Km")
print("Total kebutuhan bahan bakar untuk seluruh perjalanan =", kebutuhan_bbm, "liter")
print("Sisa bahan bakar yang ada didalam tanki motor Dimas", sisa_bbm,"liter") 
print("Jumlah bahan bakar yang harus dibeli di SPBU =", total_bbm,"liter")
print("Total biaya untuk membeli bahan bakar = RP",int(total_biaya))

#SELESAI