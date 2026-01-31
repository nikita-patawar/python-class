def main():
    fobj = None

    try:
        fobj=open("Hello1.txt","a")
        print("file gets successfully opened")

        fobj.write("Python Automation")
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()
