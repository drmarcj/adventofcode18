
from sys import stdin

sum = 0

for data in stdin:
    if data == '':
        break
    sum= sum + int(data)

print sum

