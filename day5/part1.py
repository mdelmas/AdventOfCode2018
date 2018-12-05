polymer = open("./input.txt").readline().strip()

while True :
    print(len(polymer))
    for i in range(0, len(polymer) - 1) :
        if polymer[i].capitalize() == polymer[i + 1].capitalize() and polymer[i] != polymer[i + 1] :
            polymer = polymer[:i] + polymer[i + 2:]
            break
        if i == len(polymer) - 2 :
            print(polymer, len(polymer))
            exit()

# maybe better to solve with regex
