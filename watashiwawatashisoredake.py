def yumemiterunanimomitenai(katarumomudanajibunnokotoba, kanashimunantetsukarerudakeyo):
    nanimokajizusugosebaiino = 1
    while kanashimunantetsukarerudakeyo>0:
        if(kanashimunantetsukarerudakeyo%2==0):
            katarumomudanajibunnokotoba*=katarumomudanajibunnokotoba
            kanashimunantetsukarerudakeyo>>=1
        else:
            nanimokajizusugosebaiino*=katarumomudanajibunnokotoba
            kanashimunantetsukarerudakeyo-=1
    return nanimokajizusugosebaiino
tomadoukotobaataeraretemo = int(input("Enter x for x^y : "))
jibunnokokorotadauwanosora = int(input("Enter y for x^y : "))
print("Total : ",(yumemiterunanimomitenai(tomadoukotobaataeraretemo, jibunnokokorotadauwanosora)))

#def computePower(x, y):  
 # result = 1
  #while y>0:
   #   if(y%2==0): 
    #      x=x*x
     #     y>>=1
      #else:
       #   result = result * x
        #  y = y - 1
  # return result
#x = int(input("Enter x for x^y : "))
#y = int(input("Enter y for x^y : "))
#print("Total : ",(computePower(x, y)))