a=(input("valeur A : "))
b=(input("valeur B : "))
c=(input("valeur C : "))
if (a>b) and (a>c):
    max=a
elif (b>a) and (b>c):
    max=b
else :
    max = c

print("max est : ",max)

