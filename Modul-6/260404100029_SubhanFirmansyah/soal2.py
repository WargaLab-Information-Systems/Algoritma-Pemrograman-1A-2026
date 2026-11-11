def baca_kata(pesan, jenis):
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
                print(jenis, "harus berupa teks, bukan angka, ulangi")
            continue

        return teks

print("Masukkan nama asisten awal. Ketik cukup untuk berhenti.")
daftar_awal = []
while 1:
    nama = baca_kata("Nama asisten: ", "Nama")
    if nama == "cukup":
        break
    daftar_awal.append(nama)

asisten_awal = tuple(daftar_awal)                  
print("Asisten awal :", asisten_awal)
print()

tambahan = baca_kata("Nama asisten tambahan: ", "Nama")
asisten_akhir = asisten_awal + (tambahan,)         
print("Asisten akhir:", asisten_akhir)
print()

print("Masukkan nama hari tugas. Ketik cukup untuk berhenti.")
daftar_hari = []
while 1:
    hari = baca_kata("Hari: ", "Hari")
    if hari == "cukup":
        break
    daftar_hari.append(hari)

hari_tugas = tuple(daftar_hari)
print("Hari tugas   :", hari_tugas)
print()

print("Masukkan satu pengecualian (asisten yang ada kuliah pada hari tertentu).")
nama_kecuali = baca_kata("Nama asisten pengecualian: ", "Nama")
hari_kecuali = baca_kata("Hari pengecualian: ", "Hari")

if nama_kecuali not in asisten_akhir:
    print("Catatan: nama", nama_kecuali, "tidak ada di daftar asisten")
if hari_kecuali not in hari_tugas:
    print("Catatan: hari", hari_kecuali, "tidak ada di daftar hari tugas")
print()

print("=== JADWAL SHIFT ===")
jumlah_shift = 0

for asisten in asisten_akhir:                      
    for hari in hari_tugas:                        
        if asisten == nama_kecuali and hari == hari_kecuali:
            continue                               
        jumlah_shift += 1
        print("Shift ke-", jumlah_shift, ":", asisten, "-", hari)

print()
print("Total shift yang berhasil dibuat:", jumlah_shift)