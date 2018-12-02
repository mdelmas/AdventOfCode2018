frequency = 0;
file = open("./input")

for line in file:
    frequency += int(line.strip())

print(frequency)
