import multiprocessing 
import time 
import os

def SumEven(No):
    print("Pid of sumEven: ",os.getpid()) #51
    print("PPid of sumEven: ",os.getppid())  #21
    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum + i
    print("Even sum is: ", Sum)    

def SumOdd(No):
    print("Pid of sumOdd: ",os.getpid()) # 101
    print("PPid of sumOdd: ",os.getppid())   #21
    Sum = 0
    for i in range(1,No+1,2):
        Sum = Sum + i
    print("Odd sum is: ", Sum)

def main():
    print("Pid of main : ",os.getpid())   #21
    print("PPid of main : ",os.getppid())     #CMD 11
    start_time = time.time()
    t1 = multiprocessing.Process(target = SumEven , args=(100000000,))
    t2 = multiprocessing.Process(target = SumOdd , args=(100000000,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time = time.time()

    print ("Time require: ", end_time - start_time)

if __name__ == "__main__":
    main()

