def setORnosetA(nombre, aake):
    maskk = 1
    if (aake & maskk) == 1 or (aake & maskk) == 0:
        if nombre & (1 << (aake - 1)):
            print("SET")
        else:
            print("NOT SET")
nombre = int(input("Enter the number: "))
aake = int(input("Enter the bit position: "))
setORnosetA(nombre, aake)


