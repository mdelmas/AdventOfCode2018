import re
import numpy
import itertools

file = open("./input.txt")

def parse_data(line) :
    value = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
    return {
        'id': int(value.group(1)),
        'coord': [int(value.group(2)), int(value.group(3))],
        'dim': [int(value.group(4)), int(value.group(5))],
        'overlap': False
    }

def process_grid_dim(data) :
    grid_dim = [0, 0]
    for claim in data :
        if claim['coord'][0] + claim['dim'][0] > grid_dim[0] :
            grid_dim[0] = claim['coord'][0] + claim['dim'][0]
        if claim['coord'][1] + claim['dim'][1] > grid_dim[1] :
            grid_dim[1] = claim['coord'][1] + claim['dim'][1]
    return grid_dim



data = [parse_data(line.strip()) for line in file.readlines()]
dim = process_grid_dim(data)
grid = numpy.zeros((dim[1], dim[0]))


for claim in data :
    line = list(range(claim["coord"][0], claim["coord"][0] + claim["dim"][0]))
    col = list(range(claim["coord"][1], claim["coord"][1] + claim["dim"][1]))
    for x, y in list(itertools.product(line, col)) :
        if claim['overlap'] == False and grid[y][x] == 0 :
            grid[y][x] = claim["id"]
        else if grid[y][x] > 0 :
            grid[grid == grid[y][x]] = -1
            grid[grid == claim["id"]] = -1
            grid[y][x] = -1
            claim['overlap'] = True
        else :
            grid[y][x] = -1

print("Result : " + str(grid.max()))
