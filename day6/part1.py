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

for y in range(0, height):
  for x in range(0, width):
    min = { 'id' : [], 'dist': width + height }
    for id, coord in enumerate(coords, 1) :
      dist = get_distance({ 'x': x, 'y': y }, coord)
      if dist < min['dist'] :
        min = { 'id' : [id], 'dist': dist }
      elif dist == min['dist'] :
        min['dist'] = dist
        min['id'].append(id)
    if len(min['id']) > 1 :
      grid[y][x] = 0
    else :
      grid[y][x] = min['id'][0]

zone = np.zeros(len(coords) + 1)
for id, coord in enumerate(coords, 1) :
  zone[id] = int((grid == id).sum())

for y in range(0, height) :
  zone[int(grid[y][0])] = 0
  zone[int(grid[y][width - 1])] = 0
for x in range(0, width) :
  zone[int(grid[0][x])] = 0
  zone[int(grid[height - 1][x])] = 0

# print(grid)
# print(zone)
print(max(zone))
print(list(zone).index(max(zone)))
