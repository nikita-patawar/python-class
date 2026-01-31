import gc


class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside destructor")    

# Allocate
obj1 = Demo()
obj2 = Demo()

# use

# Deallocate
del obj1  
del obj2

gc.collect()  #request to GC 

print("End of Application")