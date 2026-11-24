
print("=== SISTEM PENDAFTARAN ANGGOTA KLUB ROBOTIKA ===")

# Membuat list untuk menyimpan nama anggota
daftar_nama = []

# Memasukkan nama anggota secara berulang
while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    daftar_nama.append(nama)

# Menampilkan daftar nama yang sudah dimasukkan
print("\n=== DAFTAR CALON ANGGOTA ===")
print(daftar_nama)

# Memeriksa validitas setiap nama
print("\n=== HASIL PEMERIKSAAN NAMA ===")

for nama in daftar_nama:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid!")
    else:
        print(nama, "valid.")

# Menghapus nama yang dicurigai sebagai penyusup
print("\n=== PENGHAPUSAN ANGGOTA ===")
nama_hapus = input("Masukkan nama penyusup yang ingin dihapus: ")

if nama_hapus in daftar_nama:
    daftar_nama.remove(nama_hapus)
    print("Nama", nama_hapus, "berhasil dihapus.")
else:
    print("Nama", nama_hapus, "tidak ditemukan dalam pendaftaran.")

# Menampilkan daftar akhir
print("\n=== DAFTAR ANGGOTA SETELAH PENGHAPUSAN ===")
print(daftar_nama)
