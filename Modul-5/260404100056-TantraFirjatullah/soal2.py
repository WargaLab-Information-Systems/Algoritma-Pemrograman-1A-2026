def palindrome(kata):
    kataReverse = ''.join(reversed(kata))
    return kata == kataReverse

kata = input("Masukkan kata: ").lower()
if palindrome(kata):
    print("Kata ini adalah Palindrome")
else:
    print("Kata ini bukan Palindrome")
