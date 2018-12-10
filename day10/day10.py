import os
import string
import numpy as np
import matplotlib.pyplot as plt



# load input, strip line feeds
data = [line.rstrip('\n') for line in open('input.txt')]


nPoints=len(data)
x=[None]*nPoints
y=[None]*nPoints
dx=[None]*nPoints
dy=[None]*nPoints


for i in range(0,len(data)):
    # 1,2,4,5
    deets = data[i].replace('<',' ').replace(',',' ').replace('>',' ').\
        replace(':',' ').split()
    x[i]=int(deets[1])
    y[i]=int(deets[2])
    dx[i]=int(deets[4])
    dy[i]=int(deets[5])





for seq in range(0,10570):

    if ( seq > 10550):
#        print seq
        plt.plot(x,y,'ro')
        plt.axis([min(x)-10,max(x)+10,min(y)-10,max(y)+10])
#        plt.show()
        plt.savefig(str(seq)+'.png')
        plt.close()
    # nudge and repeat
    for i in range(0,len(data)):
        x[i]=x[i]+dx[i]
        y[i]=y[i]+dy[i]


    
