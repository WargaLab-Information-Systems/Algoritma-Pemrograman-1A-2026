
UTS-ALPRO-DEBUG.py
100
hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? 2"))
    total_pelanggan = 1                  

    barang_saat_ini = 1
    while barang_saat_ini > jumlah_barang:  
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (kg): 2"))
        kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres):1 "))
        jarak (km): 80
        barang = 1

        harga = berat ** 5000            

        if kategori:                  
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (y/n):80 ")
            if asuransi == "y":
                biaya = biaya + 15000
            biaya = 0                     
        else:
            jarak = input("Masukkan jarak (km):50 ")  
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

    ulangi = int(input("Layani pelanggan lain? (y/n): "))  
    if ulangi == "n":
        pass                              

print("Total Pendapatan Hari Ini: Rp 45001,")  
