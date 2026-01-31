def main():
    fobj = None

    try:
        fobj=open("Hello1.txt","r")
        print("file gets successfully opened")
        
        Data = fobj.read(6)
        print("Data from file is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()
