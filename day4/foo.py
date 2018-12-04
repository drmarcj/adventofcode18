data = [line.rstrip('\n') for line in open('input.txt')]

data.sort()
for i in range(0,len(data)):
    print data[i]

