import sys
import os
import time
import schedule
import shutil
import hashlib

def calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path,"rb")
    while(True):
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()
    return hobj.hexdigest()        

def BackupFiles(Source,Destination):
    copied_files = []
    print("Creating the Backup folder for Backup Process")

    os.makedirs(Destination,exist_ok=True)
    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True) 

            # copy the files if isa updated
            if( (not os.path.exists(dest_path)) or calculate_hash(src_path)!= calculate_hash(dest_path)):
                shutil.copy2(src_path,dest_path) #Copy file with metadata like created at inode
                copied_files.append(relative)
                

    return copied_files        


def MarvellousDataShieldStart(Source ="Data"):
    BackupName = "MarvellousBackup"
    print("Backup Process Started succesfully at :",time.ctime())
    files = BackupFiles(Source,BackupName)

    for name in files:
        print(name+"\n")

def main():
    Border = "_"*60
    print(Border)
    print("------------Marvellous Datashield system---------")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This script is used to :  ")
            print("1: Text auto backup at given time")
            print("2: Backup Only new and updated file")
            print("3: Create and archive of the backup periodically")
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SoueceDirectory")
            print("Time intervel: The time in minutes for periodic scheduling")
            print("SourceDirectory: Name of directory to backed up")

        else:
            print("unable to proceed as there is no such option") 
            print("plese use --h or --u to get more info")   
    
    # python demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time intervel: ",sys.argv[1])
        print("Directory name: ", sys.argv[2])
        
        # Apply a schedular

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])
        print("Data shield system started succesfully")
        print("Time Intervel in Miniutes: ",sys.argv[1])
        print("Press Control + C to stop the execution")
        #Wait Till Abort

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("unable to proceed as there is no such option") 
        print("plese use --h or --u to get more info")


    print(Border)
    print("-----------------Thank you for using our script-------------")
    print(Border)

    


if __name__ == "__main__":
    main()