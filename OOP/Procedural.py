### Def Keyword

def Addition(No1,No2):
    return No1 + No2

def Substraction(No1,No2):
    return No1 - No2


No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first No: "))
No2 = int(input("Enter secound No: "))

Ans = Addition(No1,No2)
print("Addition is: ",Ans)

Ans = Substraction(No1,No2)
print("Substraction is: ",Ans)

