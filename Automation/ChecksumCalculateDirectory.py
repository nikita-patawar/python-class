import hashlib
import os

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")
    Buffer = fobj.read(1024)
    hobj = hashlib.md5()

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()    

def DirectoryWatcher(DirectoryName="Marvellous"):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such dir")
        return
    Ret  =os.path.isdir(DirectoryName)
    if(Ret == False):
        print("There is not directory")
        return
    
    for Foldername,Subfoldername,Filename in os.walk(DirectoryName):
        for fname in Filename:
            Checksum = CalculateChecksum(os.path.join(Foldername,fname))

            print(f"File name :{fname} Cheksum: {Checksum}")




def main():
    DirectoryWatcher()
    


if __name__ == "__main__":
    main()    