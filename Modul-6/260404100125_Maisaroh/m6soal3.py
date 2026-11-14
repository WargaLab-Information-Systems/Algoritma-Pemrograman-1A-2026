jumlahPC = int(input("masukkan jumlah PC: "))  

dataPC = [] 

for i in range(jumlahPC): 
    print("\ndata PC ke-", i + 1)

    nama = input("masukkan nama PC: ")
    status = input("masukkan status PC: ")
    ram = input("masukkan kapasitas RAM: ")

    dataPC.append([nama, status, ram])

def evaluasiPC(PC):  
    ram = int(PC[2])

    if PC[1] == "normal" and ram >= 8:
        return "layak"
    else:
        return "tidak layak"

print("\n===== HASIL EVALUASI PC =====") 

for PC in dataPC:
    try:
        hasil = evaluasiPC(PC)

    except ValueError:
        hasil = "format RAM kacau"

    print('{ "PC": "' + PC[0] + '", "status": "' + hasil + '" }')
