pin_input = input("Masukkan PIN 3 digit: ").strip()
jam_input = input("Masukkan jam datang (0-23): ").strip()

if pin_input == "" or jam_input == "":
    print("PIN dan jam harus diisi.")
elif not pin_input.isdigit() or not jam_input.isdigit():
    print("PIN dan jam harus berupa angka.")
else:
    pin = int(pin_input)
    jam = int(jam_input)

    if pin < 100 or pin > 999 or jam > 23:
        print("PIN harus 3 digit dan jam harus antara 0-23.")
    else:
        digit1 = pin // 100
        digit2 = (pin // 10) % 10
        digit3 = pin % 10

        print("Digit pertama:", digit1)
        print("Digit kedua:", digit2)
        print("Digit ketiga:", digit3)

        if pin % 5 == 0:
            status = "pintu garasi terbuka" if jam < 12 else "lampu malem terbuka, lampu garasi nyala"
        elif pin % 2 == 0:
            status = "garasi terbukan buat bos" if digit1 + digit3 == digit2 else "kode genap ditolak, alarm berbunyi"
        else:
            status = "akses ditolak"

        print("Status akses pintu garasi:", status)

        cctv_status = "cctv mode malam ngerekam" if jam >= 18 else "cctv mode siang stenby"
        print("Status CCTV:", cctv_status)
