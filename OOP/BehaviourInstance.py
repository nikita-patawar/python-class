class Demo:
    No = 10

    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside instance method fun",self.Value1,self.Value2)
    
    @classmethod  #To use class methods
    def sun(cls):
        print("Inside Class method sun",cls.No)

    @staticmethod  #for use static methods
    def gun():
        print("Inside gun",Demo.No)    


Demo.sun()        

print("Class varibele No ",Demo.No)
obj = Demo(10,11)
obj.fun()

print("Instance variable: ",obj.Value1,obj.Value2)

Demo.gun()