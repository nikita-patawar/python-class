# seek(kuthe,kuthun)
#kuthun : 0/1/2
# 0: Starting
# 1: Current
# 2: End

def main():
    fobj = None

    try:
        fobj=open("Hello1.txt","rb")
        print("file gets successfully opened")
        print("Current offset is: ",fobj.tell())  #0
        fobj.seek(6,1)
        print("Current offset is: ",fobj.tell())  #11
        Data = fobj.read(6)
        print("Current offset is: ",fobj.tell()) #17
        print("Data from file is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()
