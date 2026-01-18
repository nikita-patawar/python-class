# Lambda function so it is functional approach

Checkevenodd = lambda No : (No % 2 == 0)

def main():
    Value = 0
    Ret = False
    Value = int(input("Enter a No: "))
    Ret = Checkevenodd(Value)
    if(Ret == True):
        print("No is Even")
    else:
        print("No is Odd")    

if __name__ == "__main__":
    main()