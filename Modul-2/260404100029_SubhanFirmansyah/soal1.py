print("masukkan kode anda (digit1):")
digit1 = int(input())
print("masukkan kode anda (digit2):")
digit2 = int(input())
print("masukkan kode anda (digit3):")
digit3 = int(input())
pelacakAwal = digit1 * digit3
print("pelacakan kode awal adalah :" + str(pelacakAwal))

if digit2 % 2 == 0:
    pelacak1 = pelacakAwal - digit2
else:
    pelacak1 = pelacakAwal + 25
if pelacak1 % 3 == 0:
    pelacak2 = float(pelacak1) / 3
else:
    pelacak2 = pelacak1 * 2
if pelacak2 > 50:
    print("kategori A")
else:
    if pelacak2 > 20:
        print("kategori B")
    else:
        print("sKrasnya ditolak")
        if pelacak2 % 2 == 0:
            print("siklus genap")
        else:
            print("siklus ganjil")
