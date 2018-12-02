from collections import Counter

twice = 0
thrice = 0
file = open("./input")

for line in file:
    count = dict(Counter(line.strip()))
    if 2 in count.values() :
        twice += 1
    if 3 in count.values() :
        thrice += 1

print(twice * thrice)
