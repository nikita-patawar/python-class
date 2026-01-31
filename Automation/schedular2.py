import time
import datetime
import schedule

def fun():
    print("Inside fun at: ",datetime.datetime.now())

def main():
    print("Inside marvellous automation script: ",datetime.datetime.now()) 
    schedule.every(20).seconds.do(fun)

    #problem


if __name__ == "__main__":
    main()