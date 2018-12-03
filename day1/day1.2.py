import numpy as np

sum = 0
list = np.array([])
solved = 0


# this is awful but I basically open the file and read it in 
# line by line, and if we reach the end and the solutino isn't found
# I just close it and the reopen it and start over

# clever approach would be to read it into an array and just iterate through 

while(1):
    with open("day1.input","r") as f:
        data = f.readline()
        while data:
            sum = sum + int(data)

            # this apparently is not optimal, code runs
            # increasingly slower the longer the list gets
            if sum in list:
                print 'duplicate found',sum
                solved = 1
                break

            list = np.append(list, sum)
            data = f.readline()
    f.close()

    if solved == 1:
        break





