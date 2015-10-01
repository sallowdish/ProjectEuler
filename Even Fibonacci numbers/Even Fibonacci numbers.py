__author__ = 'Ray'

#Dynamic programming table
kUpperBound = 4000000
fab = [1,2]
while(1):
    next = fab[-1] + fab[-2]
    if next <= kUpperBound:
        fab.append(next)
    else:
        break
indexes = range(1, len(fab), 3)
print(sum([fab[i] for i in indexes]))