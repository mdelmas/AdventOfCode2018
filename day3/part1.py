import re
import numpy
file = open("./input.txt")

def parse_data(line) :
    value = re.match("#\d+ @ (\d+),(\d+): (\d+)x(\d+)", line)
    return {
        'coord': [int(value.group(1)), int(value.group(2))],
        'dim': [int(value.group(3)), int(value.group(4))]
    }

def process_grid_dim(data) :
    grid_dim = [0, 0]
    for id in data :
        if id['coord'][0] + id['dim'][0] > grid_dim[0] :
            grid_dim[0] = id['coord'][0] + id['dim'][0]
        if id['coord'][1] + id['dim'][1] > grid_dim[1] :
            grid_dim[1] = id['coord'][1] + id['dim'][1]
    return grid_dim


data = [parse_data(line.strip()) for line in file.readlines()]
dim = process_grid_dim(data)

grid = numpy.zeros((dim[0], dim[1]))
overlap = 0
for id in data :
    for j in range(id['coord'][1], id['dim'][1] + id['coord'][1]) :
        for i in range(id['coord'][0], id['dim'][0] + id['coord'][0]) :
            if grid[i][j] == 1:
                overlap += 1
            grid[i][j] += 1

print(overlap)
