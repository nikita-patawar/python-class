import sys

def main():
    sum = 0
    for i in range(1,len(sys.argv)):
        sum = sum + int(sys.argv[i])
        
    print(sum)   # 1

if __name__ == "__main__":
    main()