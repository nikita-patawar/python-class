def main():
    try:
        open("Demo.txt")
        print("file gets successfully opened")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")    


if __name__ == "__main__":
    main()
