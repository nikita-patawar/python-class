# CommandLine inputs

import psutil
import sys
import os
import time
import schedule

def get_top_memory_processes(n=10):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'memory_percent']):
        try:
            # Get memory info as a named tuple
            mem_info = proc.memory_info()
            # Append process details to the list
            processes.append({
                'pid': proc.pid,
                'name': proc.info['name'],
                'rss': mem_info.rss,  # Real memory (Resident Set Size)
                'vms': mem_info.vms,  # Virtual memory (Virtual Memory Size)
                'mem_percent': proc.info['memory_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sort processes by RSS memory in descending order
    processes.sort(key=operator.itemgetter('rss'), reverse=True)
    return processes[:n]

def format_bytes(bytes_val):
    """
    Helper function to convert bytes to a human-readable format (MB).
    """
    return f"{bytes_val / (1024 * 1024):.2f} MB"
def Createlog(FolderName):
    Border = "_"*60
    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
    else:    
        os.mkdir(FolderName)
        print("Directory for log files get created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName  = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log File created with name",FileName)

    fobj = open(FileName,"w")  
    fobj.write(Border+"\n")
    fobj.write("----------------Marvellous Platform Surveillance system-----------"+"\n")
    fobj.write("Log Created at " +time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-------------------System Report--------------------\n")


    #print("CPU usage: ",psutil.cpu_percent())
    fobj.write("CPU Usage: %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    #print("Ram Usage: ",mem.percent)
    fobj.write("Ram Usage: %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\n Disk Usage Report \n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n"%(part.mountpoint,usage.percent))
        except:
            pass  


    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n") 
    fobj.write("sent : %.2f MB\n" %(net.bytes_sent/(1024 *1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv/(1024 *1024)))

    fobj.write(Border+"\n")

    #Process Log

    Data = ProcessScan()
    
    
    for info in Data:
        fobj.write("PID: %s\n" %info.get("pid"))
        fobj.write("Name: %s\n" %info.get("name"))
        fobj.write("UserName: %s\n" %info.get("username"))
        fobj.write("Status: %s\n" %info.get("status"))
        fobj.write("Start Time: %s\n" %info.get("create_time"))
        fobj.write("CPU %%:  %0.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %%:  %0.2f\n" %info.get("memory_percent"))
        fobj.write("No of threads : %s\n" %info.get("num_threads"))
        process  = psutil.Process(info["pid"])
        openFiles = process.open_files()
        fileCount = len(openFiles)
        fobj.write(Border+"\n")


    fobj.write(Border+"\n")
    fobj.write("--------------------------End of Log File-------------------------"+"\n")
    fobj.write(Border+"\n")



def ProcessScan():
    listProcess = []

    # Warm Up For CPU percent
    for p in psutil.process_iter():
        try:
            p.cpu_percent()
        except:
            pass

    time.sleep(0.2)    
    
    for proc in psutil.process_iter(attrs=["pid","name","username","status","create_time","num_threads",'memory_info','memory_percent']):
        try:

            info = proc.as_dict(attrs=["pid","name","username","status","create_time"])
            # Convert Crteate time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"  

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent() 

            listProcess.append(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listProcess

        


def main():
    Border = "_"*60
    print(Border)
    print("------------Marvellous Platform Surveillance system---------")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This script is used to :  ")
            print("1 : Create automatic logs")
            print("2 : Execute perodically")
            print("3 : end mail with logs")
            print("4 : Store information about processess")
            print("5 : Store information about Cpu")
            print("4 : Store information about Ram usage")
            print("4 : Store information about Secondary Storage ")
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("Time intervel: The time in minutes for periodic scheduling")
            print("Directory Name: Name of directory to create auto logs")

        else:
            print("unable to proceed as there is no such option") 
            print("plese use --h or --u to get more info")   
    
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time intervel: ",sys.argv[1])
        print("Directory name: ", sys.argv[2])
        
        # Apply a schedular

        schedule.every(int(sys.argv[1])).minutes.do(Createlog,sys.argv[2])
        print("Platform Surveillance system started succesfully")
        print("Directory Created with Name: ",sys.argv[2])
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