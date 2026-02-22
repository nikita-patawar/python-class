from sklearn.metrics import confusion_matrix

def main():

    # 1 Positive
    # 0 Negative
    Actual     = [1,0,1,1,1,0,1,0,0,1]
    Precdicted = [1,0,0,1,1,1,1,1,0,1]

    print("Actual Data: ",Actual)
    print("Predicted Data: ",Precdicted)

    con_mat = confusion_matrix(Actual,Precdicted)
    print(con_mat)
    
if __name__ == "__main__":
    main()   

  
