import numpy as np

serialNo = 6548

powerLevel=np.zeros((301,301))

for x in range(1,301):
    for y in range(1,301):
        rackID = x+10
        powerLevel[x][y] = (((rackID * y) + serialNo)* rackID)
        powerLevel[x][y] = (powerLevel[x][y] // (10**2)%10) - 5


## Part 1
bestx,besty = 0,0
bestPower = 0 

for x in range (1,298):
    for y in range (1,298):
    # print powerLevel[0:4,0:4]
        totalPower = sum(sum(powerLevel[x:x+3,y:y+3]))
        if totalPower > bestPower:
            bestPower = totalPower
            bestx = x
            besty = y
    

print bestx,besty, bestPower


## Part 2. I have a sneaking suspicion this is not how you do it right
## but it works so deal.
bestx,besty = 0,0
bestPower = 0

for size in range (1,300):
    print "testing grid size",size
    for x in range (1,298):
        for y in range (1,298):
    # print powerLevel[0:4,0:4]                                            
            totalPower = np.sum(powerLevel[x:x+size,y:y+size])
            if totalPower > bestPower:
                bestPower = totalPower
                bestx = x
                besty = y
                bestsize= size

print bestx,besty,bestsize, bestPower
