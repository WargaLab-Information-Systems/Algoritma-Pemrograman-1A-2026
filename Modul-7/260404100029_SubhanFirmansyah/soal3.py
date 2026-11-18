def baca_teks(pesan):
    while 1:
        teks = input(pesan)
        if teks == "":                             
            print("Input tidak boleh kosong, ulangi")
            continue

        ada_isi = False                            
        for huruf in teks:
            if huruf != " ":
                ada_isi = True
        if ada_isi == False:
            print("Input tidak boleh kosong, ulangi")
            continue

        angka_sah = False
        try:
            angka = float(teks)                    
            if angka - angka == 0:                 
                angka_sah = True
        except ValueError:
            angka_sah = False                      

        if angka_sah:
            if angka < 0:                          
                print("Input tidak boleh berupa angka negatif, ulangi")
            else:                                  
                print("Nama harus berupa teks, bukan angka, ulangi")
            continue

        return teks

def isi_himpunan(himpunan, judul):
    print("Masukkan " + judul + ". Ketik selesai untuk berhenti.")
    while 1:
        nama = baca_teks("Nama: ")
        if nama == "selesai":
            break
        if nama in himpunan:                       
            print(nama, "sudah ada, diabaikan")
        else:
            himpunan.add(nama)                     

def tampil(judul, himpunan):
    if len(himpunan) == 0:
        print(judul, ": (tidak ada)")
    else:
        print(judul, ":", himpunan)

undangan = set()
webinar_a = set()
webinar_b = set()

isi_himpunan(undangan, "nama undangan")
print()
isi_himpunan(webinar_a, "peserta Webinar A")
print()
isi_himpunan(webinar_b, "peserta Webinar B")
print()

semua_peserta = webinar_a | webinar_b              
hadir_keduanya = webinar_a & webinar_b             
hanya_satu = webinar_a ^ webinar_b                 
tidak_hadir = undangan - semua_peserta             

print("===== HASIL =====")
tampil("Semua peserta (A dan B)", semua_peserta)
tampil("Hadir di kedua webinar", hadir_keduanya)
tampil("Hanya hadir di salah satu", hanya_satu)
tampil("Undangan tidak hadir di mana pun", tidak_hadir)