import sys
import os

def DirectoryScanner(DirName="Marvellous"):
    Ret = False
    Ret =  os.path.exists(DirName)
    if(Ret == False):
        print("There is no such Directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName, SubFolderName,FileName in os.walk(DirName):

        for Fname in FileName:
            FileCount =FileCount + 1

            Fname = os.path.join(FolderName,Fname)
            print("File Name: ",Fname)
            print("File Size",os.path.getsize(Fname))
            if(os.path.getsize(Fname) == 0): #Empty
                EmptyFileCount = EmptyFileCount + 1 
                os.remove(Fname)
    Border="-"*50
    print(Border)
    print("-----------------Automation Report----------------")
    print("Total File Scanned: ",FileCount)
    print("Total empty files found: ",EmptyFileCount)
    print(Border)




def main():
    Border="-"*50
    print(Border)
    print("-------------Marvellous Directory sysyem----------")
    print(Border)
    if(len(sys.argv )!=2):
        print("Invalid no of argument")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])

    print(Border)
    print("-------------Marvellous Directory sysyem----------")
    print(Border)
    


if __name__ == "__main__" :
    main()   