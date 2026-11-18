def validasi_huruf(pesan_prompt):
    while True:
        teks = input(pesan_prompt)
        if not teks:
            print("Masukan tidak boleh kosong")
            continue
        if teks[0] == "-":
            print("Masukan tidak boleh minus")
            continue

        bukan_huruf = False
        for c in teks:
            if not ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == ' '):
                bukan_huruf = True
                break

        if bukan_huruf:
            print("Masukan tidak boleh selain huruf")
            continue

        return teks

def validasi_angka(pesan_prompt):
    while True:
        teks = input(pesan_prompt)
        if not teks:
            print("Masukan tidak boleh kosong")
            continue
        if teks[0] == "-":
            print("Masukan tidak boleh minus")
            continue

        bukan_angka = False
        for c in teks:
            if not (c >= '0' and c <= '9'):
                bukan_angka = True
                break

        if bukan_angka:
            print("Masukan tidak boleh selain angka")
            continue

        return teks

inventaris_pc = []
def evaluasi_kelayakan(pc):
    try:
        ram_angka = int(pc[2])
        if pc[1] == "Normal" and ram_angka >= 8:
            return "Layak"
        else:
            return "Tidak Layak"
    except:
        return "Format RAM Kacau"

while True:
    nama_pc = validasi_huruf("Masukkan Nama PC (ketik 'selesai' untuk berhenti): ")
    if nama_pc == "selesai":
        break

    status = validasi_huruf("Masukkan Status PC (Normal/Rusak): ")
    ram = validasi_angka("Masukkan Kapasitas RAM (GB): ")
    print()

    inventaris_pc.append([nama_pc, status, ram])

print("")
print("HASIL EVALUASI INVENTARIS PC")
for pc in inventaris_pc:
    hasil_status = evaluasi_kelayakan(pc)
    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil_status + '" }'
    print(output)
print("")