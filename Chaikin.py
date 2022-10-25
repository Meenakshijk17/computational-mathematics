from numpy import *
import matplotlib.pyplot as plt

import random
def Rand(start,end,num):
    res=[]
    for i in range(num):
        res.append(random.randint(start,end))
    return res

def smoothen(x,y):
    l=len(x)
    after_split_x=[]
    after_split_y=[]
    for i in range(l-1):
        after_split_x.append(x[i])
        after_split_x.append((x[i]+x[i+1])/2)
        after_split_y.append(y[i])
        after_split_y.append((y[i]+y[i+1])/2)
    after_split_x.append(x[l-1])
    after_split_y.append(y[l-1])
    l_split=len(after_split_x)
    average_x=[]
    average_y=[]
    for i in range(0,l_split-1,2):
        average_x.append((after_split_x[i]+after_split_x[i+1])/2)
        average_x.append(after_split_x[i+1])
        average_x.append((after_split_x[i+1]+after_split_x[i+2])/2)
        average_y.append((after_split_y[i]+after_split_y[i+1])/2)
        average_y.append(after_split_y[i+1])
        average_y.append((after_split_y[i+1]+after_split_y[i+2])/2)
    average_x.append(average_x[0])
    average_y.append(average_y[0])

    return(average_x,average_y)
    
def iterate(x,y,num):
    vertex_set_x=[x,]
    vertex_set_y=[y,]
    for i in range(num):
        #print(vertex_set_x[i],vertex_set_y[i])
        plt.plot(vertex_set_x[i],vertex_set_y[i])
        plt.show()
        new_x,new_y=smoothen(vertex_set_x[i],vertex_set_y[i])
        vertex_set_x.append(new_x)
        vertex_set_y.append(new_y)
        
m=Rand(-10,10,5)
n=Rand(-10,10,5)
m.append(m[0])
n.append(n[0])
iterate(m,n,10)