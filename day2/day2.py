import string

# a-z
letters = string.ascii_lowercase

# load input, strip line feeds
data = [line.rstrip('\n') for line in open('inputday2.txt')]

# hold duplicates/triplicates in lists sized appropriately
# initialize to zero. increment to one, and only one, if match
doubles=[0]*len(data)
triples=[0]*len(data)

# find all the doubles and triples
# repeat after me: python counts from zero!
for i in range(0, len(data)):
    for j in letters:
        # find doubles
        if data[i].count(j) == 2: 
            doubles[i] = 1
            
        elif data[i].count(j) == 3:
            triples[i] = 1
            
# and that's your answer
print sum(doubles) * sum(triples)


## Part the second
answer=''

# all of the loops
# first loop through each item
for i in range(0, len(data)):
    # next compare to each other item further down the list
    for j in range(i+1, len(data)):
        # finally find the indices of mismatching letters
        if len( [k for k in xrange(len(data[i])) 
                 if data[i][k] != data[j][k]]) == 1:
            common = [q for q in xrange(len(data[i])) 
                      if data[i][q] == data[j][q]]
            for q in range(0, len(common)):
                answer=answer+data[j][common[q]]            


# and this is your answer            
print answer










