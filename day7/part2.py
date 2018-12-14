import re
import string
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
    queue = deque()
    for c in string.ascii_uppercase :
        if c not in second_steps :
            queue.append(c)
    return queue

def get_duration(letter) :
    return 60 + ord(letter) - ord('A') + 1

def remove_step(queue, worker, steps) :
    if worker[0] in steps :
        for x in steps[worker[0]] :
            if x not in queue :
                queue.append(x)
        del steps[worker[0]]

steps = parse_data()
queue = find_starting_step(steps)
workers = [[0, 0] for x in range(5)] # w[0]: lettre, w[1]: temps
total = 0
while len(queue) > 0 or len(steps) > 0 :
    total += 1
    for worker in workers :
        if worker[1] > 0 :
            worker[1] -= 1
        if worker[1] == 0 :
            remove_step(queue, worker, steps)
            queue = deque(sorted(queue))
            curr = 0
            for i in range(len(queue)) :
                curr = queue.popleft()
                if curr in [item for i in steps for item in steps[i]] :
                    queue.append(curr)
                    curr = 0
                else :
                    break
            if curr :
                worker[0] = curr
                worker[1] = get_duration(curr)

total += max([worker[1] for worker in workers]) - 2 # can't really see why -2 and not -1
print(total)
