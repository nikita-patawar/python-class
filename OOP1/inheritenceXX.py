class Parent:
    def __init__(self):
        print('Inside parent constructor')

    def fun(self):
        print("Inside fun method of parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child construcor")

    def fun(self):
        super().fun()
        print("In side fun method of child")

cobj = Child()
cobj.fun()








