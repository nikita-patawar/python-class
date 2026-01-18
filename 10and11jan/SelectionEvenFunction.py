# Scripting approach

def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even no")
    else:
        print("It is Odd no")

def main():
    CheckEven(45)                 # Positional
    CheckEven(No = 46)            # Keyword

if __name__ == "__main__":
    main()


