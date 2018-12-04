

data = [line.rstrip('\n') for line in open('input.txt')]
class Guard:
    name = ""
    sleep = 0
    times = [0 for x in xrange(60)]
    def __init__(self, myname, mysleep):
        self.name = myname
        self.sleep = mysleep
        self.times = [0 for x in xrange(60)]

# turns out to be ridonculously easy to sort in python
data.sort()

guard=[]

# read each line

for i in range(0, len(data)):
    line = data[i].split()
     
    # if this is a guard line, create that guard if it doesn't exist
    if line[3][0] == '#':
        if any(x for x in guard if x.name == line[3]):
            pass
        else:
            guard.append(Guard(line[3],0))
        thisguard=line[3]

    # if this is a falls asleep
    # nb we only need the minutes
    if line[2] == 'falls':
        asleep= int( line[1][3:5])
    
    # if this is awake... 
    if line[2] == 'wakes':
        awake= int( line[1][3:5])
        for i in range(0,len(guard)):
            if (guard[i].name==thisguard):
                guard[i].sleep = guard[i].sleep + (awake-asleep)

                for j in range(asleep, awake):
                    guard[i].times[j]= guard[i].times[j]+1
#                print guard[i].name, guard[i].sleep, asleep, awake, guard[i].times[0:5]
    
biggest = 0
for i in range(0,len(guard)):
    if guard[i].sleep > biggest:
        biggest = guard[i].sleep
        winner = i

#print guard[winner].times
print "laziest guard is",
print guard[winner].name ,  
print "most sleep was", max(guard[winner].times), "times at", guard[winner].times.index(max(guard[winner].times)),
print "minutes after midnight"


#for i in range(0,len(guard)):
#    print guard[i].name
#    for j in range(0,40):
#        print guard[i].times[j],
#    print


    
