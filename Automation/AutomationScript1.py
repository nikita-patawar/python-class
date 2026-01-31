import sys


def main():
    Border = "-"*40
    print(Border )
    print("__________Marvellous Automation_________")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is use to perform ____")
            print("This is Automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the keyword script as ")
            print("scriptName.py Argument1 Argument2")  
            print("Argument1: ________")
            print("Argument2: _________")  
        else:
            print("Use the given flags as: ")        
            print("--u: Used to dispaly usage")
            print("--h: Used to dispaly Help")
    else:
        print("invalid no of command Line Arguments ")
        print("Use the given flags as: ")        
        print("--u: Used to dispaly usage")
        print("--h: Used to dispaly Help")
        print(Border )
    print(Border )
    print("_____Thank ypu for using our script_____")
    print("__________Marvellous Infosysyems________")
    print(Border)    
               

if __name__ == "__main__":
    main()    