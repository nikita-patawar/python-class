import gc


class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside destructor")    

# Allocate
obj = Demo()

# use

# Deallocate
del obj  

gc.collect()  #request to GC 

print("End of Application")