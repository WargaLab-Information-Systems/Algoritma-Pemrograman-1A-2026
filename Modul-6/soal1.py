# program pendaftaran anggota klub robotika

def input_nama(pesan):
    while True:
        nama = input(pesan).strip()

        if nama == "":
            print("Nama tidak boleh kosong.")
        elif "-" in nama:
            print("Tanda '-' tidak boleh digunakan.")
        elif nama.isdigit():
            print("Masukkan huruf, bukan angka.")
        else:
            return nama


nama_list = []

# minta input nama terus sampai ketik "selesai"
nama = input_nama("Masukkan nama (ketik selesai untuk berhenti): ")
while nama != "selesai":
    nama_list.append(nama)
    nama = input_nama("Masukkan nama (ketik selesai untuk berhenti): ")

print("")
print("Hasil pengecekan:")
for n in nama_list:
    if n == "admin" or len(n) < 4:
        print(n, "-> nama tidak valid")
    else:
        print(n, "-> nama valid")

# hapus nama penyusup
print("")
penyusup = input_nama("Masukkan nama penyusup yang mau dihapus: ")

if penyusup in nama_list:
    nama_list.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus")
else:
    print("Nama", penyusup, "tidak ada di pendaftaran")

# tampilkan daftar terakhir
print("")
print("Daftar nama sekarang:")
for n in nama_list:
    print(n)