import sys

def main():
    if(len(sys.argv) < 3 or len(sys.argv)>3):
        print("Invalid no of arguments")
    else:
        No1 = int(sys.argv[1]) 
        No2 = int(sys.argv[2])  

        print("Addition is: ",No1+No2) 


if __name__ == "__main__":
    main()