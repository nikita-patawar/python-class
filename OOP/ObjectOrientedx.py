class Arithematic:

    def Addition(self,No1,No2):
        return No1 + No2

    def Substraction(self,No1,No2):
        return No1 - No2

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first No: "))
No2 = int(input("Enter secound No: "))
obj = Arithematic()

Ans = Arithematic().Addition(No1,No2)
print("Addition is: ",Ans)

Ans = Arithematic().Substraction(No1,No2)
print("Substraction is: ",Ans)