def main():
    fobj = None

    try:
        fobj=open("Hello1.txt","w")
        print("file gets successfully opened")

        fobj.write("jay ganesh Marvelous")
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()
