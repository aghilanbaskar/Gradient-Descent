import numpy as np

def find_x_and_y(X,Y,x_min,x_max,y_min,y_max):
    x=[]
    y=[]
    for d in X:
        temp=(d-x_min)/(x_max-x_min)
        x.append(temp)
    for d in Y:
        temp=(d-y_min)/(y_max-y_min)
        y.append(temp)
    return x,y

def find_yp_sse_dela_delb(a,b,x,y):
    yp=[]
    sse=[]
    del_a=[]
    del_b=[]
    for d in x:
        temp=(a)+(b*d)
        yp.append(temp)
    for i in range(len(yp)):
        temp=((y[i]-yp[i])**2)/2
        sse.append(temp)
    for i in range(len(yp)):
        temp=-(y[i]-yp[i])
        del_a.append(temp)
    for i in range(len(yp)):
        temp=-((y[i]-yp[i])*x[i])
        del_b.append(temp)
    return yp,sse,del_a,del_b


if __name__ == '__main__':
    data = np.genfromtxt ('data.csv', delimiter=",")
    X=data[:,0]
    Y=data[:,1]
    x,y=find_x_and_y(X,Y,np.min(X),np.max(X),np.min(Y),np.max(Y))
    a=0.5 #random a value
    b=0.5 #random b value
    learning_rate=0.001 #learning rate

    #finding a and b value, and sse error
    yp,sse,del_a,del_b=find_yp_sse_dela_delb(a,b,x,y)
    sse_error=np.sum(sse)
    a=a-(learning_rate*np.sum(del_a))
    b=b-(learning_rate*np.sum(del_b))
    #print(,sse_error,a,b)


    #inding new a and b value and minimised sse error
    yp,sse,del_a,del_b=find_yp_sse_dela_delb(a,b,x,y)
    new_sse_error=np.sum(sse)
    new_a=a-(learning_rate*np.sum(del_a))
    new_b=b-(learning_rate*np.sum(del_b))
    #print(new_sse_error,new_a,new_b)


    while new_sse_error < sse_error:
        #print(new_sse_error,':',sse_error)
        sse_error=new_sse_error
        a=new_a
        b=new_b
        yp,sse,del_a,del_b=find_yp_sse_dela_delb(new_a,new_b,x,y)
        new_sse_error=np.sum(sse)
        new_a=a-(learning_rate*np.sum(del_a))
        new_b=b-(learning_rate*np.sum(del_b))
        #print(new_sse_error,new_a,new_b)
    
    
    print('a:',a,'\nb:',b,' with minimised SSE:',sse_error)
