import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = np.genfromtxt ('data.csv', delimiter=",")
    X=data[:,0]
    Y=data[:,1]
    x_train = X.reshape(-1,1)
    y_train = Y.reshape(-1,1)

    #find a and b
    n=len(y_train)
    l_r=0.0001 #learning rate
    a = np.zeros((n,1))
    b = np.zeros((n,1))
    
    epochs = 0
    while(epochs < 1000):
        y = a +(b * x_train)
        error = y - y_train
        mean_sq_er = np.sum(error**2)
        mean_sq_er = mean_sq_er/n
        a = a - l_r * np.sum(error)/n
        b = b - l_r * np.sum(error * x_train)/n
        epochs += 1
        if(epochs%1000==0):
            print(mean_sq_er)

    a=np.sum(a)/n
    b=np.sum(b)/n
    print(a,b)
    
    y_pred=[]
    for i in range(n):
        y_predict=a+(b*x_train[i])
        y_pred.append(y_predict)
        print('y:',y_train[i],'predicted_y:',y_predict)
    print('final_accuracy:',r2_score(y_train,y_pred))

    y_plot = []
    for i in range(100):
        y_plot.append(a + b * i)
    plt.figure(figsize=(10,10))
    plt.scatter(x_train,y_train,color='red',label='GT')
    plt.plot(range(len(y_plot)),y_plot,color='black',label = 'pred')
    plt.legend()
    plt.show()
