
import sys
import os
import time
import schedule

def fun(DirName):
    pass

def main():
    Border = "_"*60
    print(Border)
    print("------------Marvellous Datashield system---------")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This script is used to :  ")
            print("1: Text auto backup at given time")
            print("2: Backup Only new and updated file")
            print("3: Create and archive of the backup periodically")
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SoueceDirectory")
            print("Time intervel: The time in minutes for periodic scheduling")
            print("SourceDirectory: Name of directory to backed up")

        else:
            print("unable to proceed as there is no such option") 
            print("plese use --h or --u to get more info")   
    
    # python demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time intervel: ",sys.argv[1])
        print("Directory name: ", sys.argv[2])
        
        # Apply a schedular

        schedule.every(int(sys.argv[1])).minutes.do(fun,sys.argv[2])
        print("Data shield system started succesfully")
        print("Time Intervel in Miniutes: ",sys.argv[1])
        print("Press Control + C to stop the execution")
        #Wait Till Abort

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("unable to proceed as there is no such option") 
        print("plese use --h or --u to get more info")


    print(Border)
    print("-----------------Thank you for using our script-------------")
    print(Border)

    


if __name__ == "__main__":
    main()