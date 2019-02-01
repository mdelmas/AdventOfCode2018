import re
import numpy as np
import string

def parse_data(line) :
    value = re.match("(\d+), (\d+)", line)
    return {
        'x': int(value.group(1)),
        'y': int(value.group(2))
    }

coords = [parse_data(line.strip()) for line in open("./input.txt").readlines()]

width = max(coord['x'] for coord in coords) + 1
height = max(coord['y'] for coord in coords) + 1
grid = np.zeros((height, width))

def get_distance(p1, p2) :
  return abs(p1['x'] - p2['x']) + abs(p1['y'] - p2['y'])

for y in range(0, height) :
  for x in range(0, width) :
    sum_dist = 0
    for id, coord in enumerate(coords, 1) :
      sum_dist += get_distance({ 'x': x, 'y': y }, coord)
    if sum_dist < 10000 :
      grid[y][x] = 1

print(grid)
print((grid == 1).sum())
