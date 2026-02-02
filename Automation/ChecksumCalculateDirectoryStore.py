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

def FindDuplicate(DirectoryName="Marvellous"):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such dir")
        return
    Ret  =os.path.isdir(DirectoryName)
    if(Ret == False):
        print("There is not directory")
        return
    
    Duplicate = {}
    for Foldername,Subfoldername,Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(Foldername,fname)
            Checksum = CalculateChecksum(fname)
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
   
    return Duplicate

# def DisplayResult(MyDict):
#     Result = list(filter(lambda x: len(x) > 1,MyDict.values()))

#     Count = 0

#     for value in Result:
#         for subvalue in value:
#             Count = Count + 1
#             print(subvalue)
#         print("Value of count is: ",Count) 
#         Count = 0   


def DeleteDuplicate(path ="Marvellous"):
    MyDict = FindDuplicate(path)
    Result = list(filter(lambda x: len(x) > 1,MyDict.values()))
    print(Result)

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted File: " ,subvalue)
                os.remove(subvalue)
                Cnt = Cnt +1
        Count = 0
    print("Total deleted File: ",Cnt)            


    

def main():
    # FindDuplicate()
     DeleteDuplicate()

    
if __name__ == "__main__":
    main()    