# [A,B,C,D]
#X[1,2,3,5]
#Y[2,3,1,6]
# [R,R,B,B]

#Predict(3,3) ---> ?
import numpy as np
import math

def EuDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def MarvellousKneighborsClassifier():
    border = "-"*50
    data = [
                {'point':"A", "X":1, "Y":2, "Label":"Red"},
                {'point':"B", "X":2, "Y":3, "Label":"Red"},
                {'point':"C", "X":3, "Y":1, "Label":"Blue"},
                {'point':"D", "X":5, "Y":6, "Label":"Blue"}
            ]
    print(border)
    print("Marvellous UserDefined KNN")
    print(border)
    print(border)
    print("Training Data Set")
    print(border)
    new_point = {'X':3,'Y':3}

    for d in data:
        d['distance'] = EuDistance(d,new_point)    
    print(border)
    print("Calculated distances are : ",)
    print(border)
    for d in data:
        print(d)

        
def main():
    MarvellousKneighborsClassifier()


if __name__ == "__main__":
    main()

