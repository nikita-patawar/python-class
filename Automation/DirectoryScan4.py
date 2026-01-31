import os

def Directoryscanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False ):
        print("There is no such directory")
        return
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False ):
        print("Unable to scan dir as it is not directory")
        return
    
    print("Contents of the directory are : ")
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder name: ",FolderName)
        for subf in SubFolderName:
            print("Sub Folder Name: ",subf)

        for fname in FileName:
            print("File name: ",fname)    




def main():
    DirectoryName = input("Enter the name of directory: ")
    Directoryscanner(DirectoryName)



if __name__ == "__main__":
    main()