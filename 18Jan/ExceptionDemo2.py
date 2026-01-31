def main():
    Ans = 0
    try:
        print("Inside Try")
        print("Enter first No")
        No1 = int(input())

        print("Enter Secound No2")
        No2 = int(input())
    
        
        Ans = No1 / No2

    except:
        print("inside Except")

    finally:
        print("Inside finally")    


    print("Division is: ",Ans)



if __name__ == "__main__":
    main()    