import re
import numpy as np
import string
import operator
from collections import deque


def parse_data() :
    steps = {}
    for line in open("./input.txt").readlines() :
        values = re.match("Step ([A-Z]) must be finished before step ([A-Z]) can begin.", line)
        if values.group(1) not in steps :
            steps[values.group(1)] = []
        steps[values.group(1)].append(values.group(2))
        steps[values.group(1)].sort()
    return steps

def find_starting_step(steps) :
    second_steps = [item for i in steps for item in steps[i]]
    # print(sorted(set(second_steps)))
    queue = deque()
    for c in string.ascii_uppercase :
        if c not in second_steps :
            queue.append(c)
    return queue

steps = parse_data()
queue = find_starting_step(steps)
result = ""
while len(queue) > 0 :
    print(queue)
    print(result)
    print(steps)
    print()
    curr = queue.popleft()
    while curr in [item for i in steps for item in steps[i]] :
        queue.append(curr)
        curr = queue.popleft()

    if curr in steps :
        for x in steps[curr] :
          if x not in queue :
            queue.append(x)
        del steps[curr]
    queue = deque(sorted(queue))
    result += curr

print(result)

#
# print(start)
# print(steps)
# queue = deque([start])
# result = ""
# print(start)
# while len(queue) > 0 :
#   c = queue.popleft()
#   print(c)
#
#   for step in steps :
#     if step[1] == c and step[0] not in result :
#       queue.append(c)
#       c = 0
#       break
#
#   if c :
#     for step in steps :
#       if step[0] == c and step[1] not in queue :
#         queue.append(step[1])
#
#     queue = deque(sorted(queue))
#     print(queue)
#     result += c
#
# print('resultt : ' + result)
