import string
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


# I go from zero to N where N is just past my target
for seq in range(0,10570):

    # don't bother outputing stuff before 10550, it's garbage
    # answer is at 10558, found by trial and error.
    if ( seq > 10550):
        plt.plot(x,y,'ro')
        # flip the Y axis, origin is TL
        plt.axis([min(x)-10,max(x)+10,max(y)+10,min(y)-10])
        plt.savefig(str(seq)+'.png')
        plt.close()
    # nudge and repeat
    for i in range(0,len(data)):
        x[i]=x[i]+dx[i]
        y[i]=y[i]+dy[i]


    
