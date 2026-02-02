import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")
    Buffer = fobj.read(1024)
    hobj = hashlib.md5()

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()    

def main():
    Checksum = CalculateChecksum("Demo.txt")
    print(Checksum)


if __name__ == "__main__":
    main()    