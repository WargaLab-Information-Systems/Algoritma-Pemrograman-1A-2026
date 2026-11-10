
hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 1                  

    barang_saat_ini = 1
    while barang_saat_ini > jumlah_barang:  
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (kg): "))
        kategori = str(input("Pilih kategori (1. Standar / 2. Ekspres): "))

        harga = berat ** 5000            

        if kategori == 2:                  
            biaya = 20000
            asuransi = (input("Tambahkan asuransi? (y/n): "))
            if asuransi == "y":
                biaya = biaya + 15000
            biaya = 0                     
        else:
            jarak = int(input("Masukkan jarak (km): ")) 
            if jarak > 100:
                biaya = 15000
            if jarak > 20:                
                biaya = 10000
            else:
                biaya = 5000

        total_barang = harga % biaya      
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini * 1  

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan

    ulangi = str(input("Layani pelanggan lain? (y/n): "))  
    if ulangi == "n":
        pass                              

print("Total Pendapatan Hari Ini: Rp", total_revenue)


"""
1. di if kategori = 2 itu seharusnya sama dengannya dua karena oitu sama dengannya ada dua sebagai perbandingan antar kategori dan angka 
2. di elsenya itu bawahnya kan ada jarak yang nah setelah jarak harusnya dan sama dengan harusnya tambahkan int karena yang dimasukan itu bilangan bulat dan 
ditambahkan kurungnya supaya tau programnya yang dibaca
3. di kategori dimana disitu ada tulisannya nya pilih katogri awalnya itu itnt itu salah diganti jadi str karena yang dimasukin itu kata bukan bilangan bulat 
4. yang di terakhir tulisan ulangi = itu harusnya str tapi malah int karena yang diminta itu kata bukan bilangan bulat 
5.

"""