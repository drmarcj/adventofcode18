import sys





## read the sentence into a list of ints
data = [line.rstrip('\n') for line in open('input.txt')]
sentence = [int(i) for i in data[0].split()]

# allow me to traverse a tree at least N deep where N is way massively
# overestimated as the length of the input string

sys.setrecursionlimit(len(sentence))

i=-1
metadata=[]

## "next value" function returns the next value
def next_val():
    global i 
    i += 1
    return sentence[i]


## parse tree function gets the number of children
## and populates a metadata list 
def parse_tree():
    global metadata
    children = next_val()
    meta_count = next_val()
    for _ in range(children):
        print children,
        parse_tree()
    for _ in range(meta_count):
        metadata.append(next_val())


parse_tree()
print sum(metadata)
