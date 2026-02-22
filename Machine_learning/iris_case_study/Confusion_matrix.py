from sklearn.datasets import load_iris

def main():
    print("Iris Classification case study")

    DataSet = load_iris()

    Border = "-"*40

    for i in range(len(DataSet.target)):
        print("ID %d, Feature %s, Label %d" %(i,DataSet.data[i], DataSet.target[i]))

    
if __name__ == "__main__":
    main()   

  
