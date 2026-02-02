import sys
import os
import time
import schedule

def DirectoryScanner(DirName="Marvellous"):
    Border="-"*50
    timestamp = time.ctime()
    Logfilename = "Marvellous%s.log" %(timestamp)
    Logfilename = Logfilename.replace(" ","_")
    Logfilename = Logfilename.replace(":","_")

    fobj = open(Logfilename,"w")
    fobj.write(Border+"\n")
    fobj.write("This is log file created by Marvellius automation\n")
    fobj.write("This is Direvtory cleaner script\n")
    fobj.write(Border+"\n")
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

            if(os.path.getsize(Fname) == 0): #Empty
                EmptyFileCount = EmptyFileCount + 1 
                os.remove(Fname)

    fobj.write("Total File Scanned: "+str(FileCount)+"\n")
    fobj.write("Total empty files found: "+str(EmptyFileCount)+"\n")
    fobj.write("This log file created at :"+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.close()



def main():
    Border="-"*50
    print(Border)
    print("-------------Marvellous Directory sysyem----------")
    print(Border)
    if(len(sys.argv )!=2):
        print("Invalid no of argument")
        print("Please specify the name of directory")
        return
    

    schedule.every(1).minute.do(DirectoryScanner)

    while(True):
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("-------------Marvellous Directory sysyem----------")
    print(Border)
    


if __name__ == "__main__" :
    main()   