while True :
    n = int(input("masukkan jumlah angka(2-15) = "))
    if n >= 2 and n <= 15 :
        break
    else :
        print ("ulangi di luar rentang")

for i in range( n + 1):
    print(" " * ( n - i), end = "")    
    
    for a in range(1,i + 1) :
        print(a % 10, end = "")

    for a in range(i - 1 ,0 ,-1):
        print(a%10 , end = "")                                           
    print()

for i in range(n - 1,0,-1):
    print(" " * (n - i), end = "")

    for b in range(1, i + 1) :
        print(b% 10, end = "")

    for b in range(i-1,0, -1) : 
        print(b% 10, end = "")
    
