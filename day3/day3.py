import string
import numpy as np

# that's your big ole matrix, initialized to zero
matrix=np.zeros([1000,1000],dtype=int)

# number of tiles with > 1 elf
answer = 0

# load input, strip line feeds
data = [line.rstrip('\n') for line in open('input.txt')]


for i in range(0,len(data)):
    # that's right I went there
    deets = data[i].replace('@',' ').replace(',',' ').replace('x',' ').replace(':',' ').split()
    


    # fill in the square - right now just increment rather than attribute
    # a square to an elf
    for j in range(int(deets[1]),int(deets[1])+int(deets[3])):
        for k in range(int(deets[2]),int(deets[2])+int(deets[4])):
            matrix[j][k]+=1
    
for j in range(0,1000):
    for k in range(0,1000):
        if (matrix[j][k] > 1):
            answer=answer+1

print answer
        

## Part the second

# look at each claim, add up elements.
# Then look at the matrix at that location and add up elements
# if it matches you're golden


# start back at the start

for i in range(0,len(data)):
    total=0
    deets = data[i].replace('@',' ').replace(',',' ').replace('x',' ').\
        replace(':',' ').split()
    for j in range(int(deets[1]),int(deets[1])+int(deets[3])):
        for k in range(int(deets[2]),int(deets[2])+int(deets[4])):
            if matrix[j][k] > 0:
                total=total+matrix[j][k]
    extent = int(deets[3])*int(deets[4])

##    print deets,total,extent 
    if total==extent:
        print 'winner! ',deets
        # debug, print the 'winning' patch
#        for j in range(int(deets[1]),int(deets[1])+int(deets[3])):
#            for k in range(int(deets[2]),int(deets[2])+int(deets[4])):
#                print matrix[j][k],
#            print ''
