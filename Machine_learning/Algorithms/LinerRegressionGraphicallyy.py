import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent variables : X  - ",X)
    print("Values of Dependent variables : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_MEAN is :",mean_x) # 3.0
    print("Y_MEAN is :",mean_y) # 3.6

    n = len(X)                  #5

    # Y = mX + C

    # m =(summ(x-x_bar) * (y-y_bar))  / (Sum(X- X_bar) **2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denominator = denominator + ((X[i]-mean_x) **2)
    print(denominator)

    m = numerator /denominator 

    print("Slope of line ie m : ",m)   # 0.4

    C = mean_y - m * mean_x
    print("Y intercept of line C is: ",C)

    x = np.linspace(1,6,n)
    print(x)
    y = C + m *x
    print(y)
    plt.plot(x,y,color = 'g',label = "Regressionline")
    plt.scatter(X,Y,color = 'r',label ="scatter plot")

    plt.xlabel("X : Independent variables")
    plt.ylabel("Y Dependent Variable")
    plt.legend()
    plt.show()

    #cal culayr yp and yp_bar
    yp = list()
    for i in range(n):
        v = m * X[i] + C 
        yp.append(v)
    print(yp)  

    mean_yp = np.mean(yp)
    print(mean_yp)  


def main():
    MarvellousPredictor()


if __name__ == "__main__":
    main()    