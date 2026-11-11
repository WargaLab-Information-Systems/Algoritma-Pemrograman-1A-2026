def baca_nama(pesan):
    while 1:
        nama = input(pesan)
        if nama == "":                             
            print("Input tidak boleh kosong, ulangi")
            continue

        ada_isi = False                            
        for huruf in nama:
            if huruf != " ":
                ada_isi = True
        if ada_isi == False:
            print("Input tidak boleh kosong, ulangi")
            continue

        angka_sah = False
        try:
            angka = float(nama)                    
            if angka - angka == 0:                 
                angka_sah = True
        except ValueError:
            angka_sah = False                      

        if angka_sah:
            if angka < 0:                          
                print("Input tidak boleh berupa angka negatif, ulangi")
            else:                                  
                print("Input harus berupa nama, bukan angka, ulangi")
            continue

        return nama

daftar = []                                        

print("Masukkan nama calon anggota. Ketik selesai untuk berhenti.")
while 1:
    nama = baca_nama("Nama calon anggota: ")
    if nama == "selesai":
        break
    daftar.append(nama)                            

print()

if len(daftar) == 0:
    print("Belum ada calon anggota yang terdaftar")
else:
    print("=== EVALUASI NAMA ===")
    for nama in daftar:
        if nama == "admin" or len(nama) < 4:
            print(nama, ": nama tidak valid")
        else:
            print(nama, ": valid")
    print()

    print("Ketik nama penyusup yang akan dihapus.")
    print("Ketik selesai jika sudah tidak ada penyusup lagi.")
    penyusup_terhapus = 0

    while 1:
        penyusup = baca_nama("Nama penyusup: ")
        if penyusup == "selesai":
            break

        jumlah = 0
        while 1:
            try:
                daftar.remove(penyusup)            
                jumlah += 1
            except ValueError:
                break                              

        if jumlah > 0:
            penyusup_terhapus += 1
            print(penyusup, "dihapus dari pendaftaran (", jumlah, "data)")
        else:
            print("Nama", penyusup, "tidak ditemukan dalam pendaftaran")

        if len(daftar) == 0:                       
            print("Daftar pendaftaran sudah kosong")
            break

    print()
    print("Penyusup yang berhasil dihapus:", penyusup_terhapus, "nama")
    print("Daftar akhir:", daftar)