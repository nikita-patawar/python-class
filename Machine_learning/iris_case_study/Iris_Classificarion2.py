from sklearn.datasets import load_iris

def main():
    print("Iris Classification case study")

    DataSet = load_iris()

    #Metadeta of datasets 
    print("Independent variables are:")
    print(DataSet.feature_names)

    print("Dependent variables are:")
    print(DataSet.target_names)
   

if __name__ == "__main__":
    main()   

  
