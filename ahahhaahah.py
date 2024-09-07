#1 and zeeeroos ahaHAHAHAHHAHAAHAHHAHAHAAHHAHAHAHAHAHAHAHA
def NUMBEROBBITSSSSSSSAHAHHAHA(AHA):
    ones = 0
    zeros = 0
    while (AHA):
        if (AHA&1 == 1):
            ones+=1
        else:
            zeros+=1
        AHA >>= 1
        print("numbe o ones", ones, "numbe o zeros = ", zeros)

number = int(input("Enter your number: "))
NUMBEROBBITSSSSSSSAHAHHAHA(number)