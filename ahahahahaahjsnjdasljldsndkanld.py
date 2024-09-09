def po8(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 8 != 0):
                return False
            n = n // 8
            
    return True
moshiwatashikaraugakunonaraba = int(input("Subete kaeru no nara koro ni suru"))
if po8(moshiwatashikaraugakunonaraba) == False:
     print("Konna jibun ni mirai wa aru no? (no)")
else:
    print("Konna sekai ni watashi wa iru no? (yes)")