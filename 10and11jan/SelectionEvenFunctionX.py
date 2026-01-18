# Procedural approach

def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even no")
    else:
        print("It is Odd no")

def main():
    Value = 0
    Value = int(input("Enter a No: "))
    CheckEven(Value)

if __name__ == "__main__":
    main()


