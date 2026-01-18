import time

def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact        

def main():
    Value = int(input("Enter NO:  "))
    start_time = time.time()
    Ans = Factorial(Value)
    end_time = time.time()
    print("Factorial is: ",Ans)
    print("Total execution time is : ",end_time - start_time)

if __name__ == "__main__":
    main()

