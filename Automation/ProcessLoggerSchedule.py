# CommandLine inputs

import psutil
import sys
import os
import time
import schedule

def Createlog(FolderName):
    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
    else:    
        os.mkdir(FolderName)
        print("Directory for log files get created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName  = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log File created with name",FileName)

    fobj = open(FileName,"w")  

def main():
    Border = "_"*60
    print(Border)
    print("------------Marvellous Platform Surveillance system---------")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This script is used to :  ")
            print("1 : Create automatic logs")
            print("2 : Execute perodically")
            print("3 : end mail with logs")
            print("4 : Store information about processess")
            print("5 : Store information about Cpu")
            print("4 : Store information about Ram usage")
            print("4 : Store information about Secondary Storage ")
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("Time intervel: The time in minutes for periodic scheduling")
            print("Directory Name: Name of directory to create auto logs")

        else:
            print("unable to proceed as there is no such option") 
            print("plese use --h or --u to get more info")   
    
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time intervel: ",sys.argv[1])
        print("Directory name: ", sys.argv[2])
        
        # Apply a schedular

        schedule.every(int(sys.argv[1])).minutes.do(Createlog,sys.argv[2])
        print("Platform Surveillance system started succesfully")
        print("Directory Created with Name: ",sys.argv[2])
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