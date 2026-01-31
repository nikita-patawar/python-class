import gc


class Demo:
    # Class variable
    No1 = 10
    No2 = 11

    def __init__(self):

        # Instance variable
        self.A = 101
        self.B = 201
        print("Inside constructor")

    def __del__(self):
        print("Inside destructor")   



print(Demo.No1)        
print(Demo.No2) 

obj1 = Demo()
print(obj1.A)
print(obj1.B)
