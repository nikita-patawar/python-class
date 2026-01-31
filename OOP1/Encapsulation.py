class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        print("Object get created succesfully")

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
obj1 = Arithmatic(10,100)    #Arithmatic(id(obj1),10,100)
obj2 = Arithmatic(11,10)  

ret=obj1.Addition()  #Addition(id(obj1))  -> Addition(1000)   It will passs address
print(ret)

Ret = obj2.Substraction()
print(Ret)


