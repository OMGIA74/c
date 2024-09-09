def po4(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
            
    return True
mienaiwasoushiranai = int(input("Jibun kara ugoku koto mo naku "))
if po4(mienaiwasoushiranai) == False:
     print("Toki no sukima ni nagasare tsuzukete (no)")
else:
    print("Shiranai wa mawari no koto nado (yes)")