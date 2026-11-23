data_absensi = [
    ("Andi", "Hadir"), 
    ("Citra", "Hadir"), 
    ("Fajar", "Hadir"), 
    ("Budi", "Izin"), 
    ("Eko", "Izin"), 
    ("Dina", "Alpa"), 
    ("Gina", "Alpa")]
hadir = []
izin = []
alpa = []
for nama, status in data_absensi:
    if status == "Hadir":
        hadir.append(nama)
    elif status == "Izin":
        izin.append(nama)
    else:
        alpa.append(nama)

print("=== HASIL ABSENSI MAHASISWA ===")
print("Mahasiswa Hadir:", hadir)
print("Mahasiswa Izin:", izin)
print("Mahasiswa Alpa:", alpa)
