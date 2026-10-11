suhu_kritis = 1000
suhu_pompa_maksimal = 800
suhu_panas = 500
tekanan_meltdown = 50
tekanan_tidak_stabil = 30

suhu = input("Suhu reaktor (Celcius): ").strip()
tekanan = input("Tekanan gas (Bar): ").strip()

if suhu == "" or tekanan == "":
    print("Suhu dan tekanan tidak boleh kosong.")
elif not suhu.lstrip("-").isdigit() or not tekanan.lstrip("-").isdigit():
    print("Suhu dan tekanan harus berupa angka.")
else:
    suhu = int(suhu)
    tekanan = int(tekanan)

    if suhu > suhu_kritis:
        status = "MELTDOWN! SEGERA EVAKUASI!" if tekanan > tekanan_meltdown else "Bahaya Suhu: Segera Turunkan Daya!"
    elif suhu > suhu_panas:
        status = "Peringatan: Tekanan Tidak Stabil" if tekanan > tekanan_tidak_stabil else "Operasi Reaktor Normal"
    else:
        status = "Reaktor Belum Cukup Panas"

    pompa = "Pompa Maksimal" if suhu > suhu_pompa_maksimal else "Pompa Normal"

    print("Suhu    :", suhu, "Celcius")
    print("Tekanan :", tekanan, "Bar")
    print("Status  :", status)
    print("Pompa   :", pompa)