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
    
    for FolderName, SubFolderName,FileName in os.walk(DirName):
        for Fname in FileName:
            Fname = os.path.join(FolderName,Fname)
            print("File Name: ",Fname)
            print("File Size",os.path.getsize(Fname))


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
    


if __name__ == "__main__" :
    main()   