frequency = 0;
seen_frequencies = {0} # set faster than list
found = False
# alternative solution :
# data = [int(x) for x in open("input.txt").readlines()]
# for num in itertools.cycle(data):

while not found:
    file = open("./input")
    for line in file:
        frequency += int(line.strip())
        if frequency in seen_frequencies:
            found = True
            break
        else:
            seen_frequencies.add(frequency)
    file.close()

print(frequency)
