# Procedural approach

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False
    Value = int(input("Enter a No: "))
    Ret = CheckEven(Value)
    if(Ret == True):
        print("No is Even")
    else:
        print("No is Odd")    

if __name__ == "__main__":
    main()


