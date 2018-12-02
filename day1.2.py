
from sys import stdin
import numpy as np

sum = 0
list = np.array([])
solved = 0
x=1

while(1):
    with open("day1.input","r") as f:
        data = f.readline()
        while data:
            sum = sum + int(data)
            # print sum

            if sum in list:
                print 'duplicate found',sum
                solved = 1
                break

            list = np.append(list, sum)
            data = f.readline()
    f.close()

    print "end of round ", x
    x=x+1
    print len(list)
    if solved == 1:
        break





