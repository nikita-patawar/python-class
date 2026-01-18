from FMRModule import filterX,mapX,reduceX

CheckEven = lambda No: (No % 2 == 0)
Increment = lambda No: (No + 1)
Add = lambda A,B: A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data id: ",Data)

    FData = list(filterX(CheckEven,Data))   #Filter always Returns bollean
    print("Data after filter is :",FData)

    MData = list(mapX(Increment,FData))
    print("Data after map is: ",MData)

    RData = reduceX(Add,MData)
    print("Data after reduce is :",RData)


if __name__ == "__main__":
    main() 
