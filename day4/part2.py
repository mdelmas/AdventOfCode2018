import re

data = [line.strip() for line in open("./input.txt").readlines()]
data.sort()

slept = {}
for line in data :
  if '#' in line :
    id = int(re.findall(r"\#(\d+)", line)[0])
    if id not in slept :
      slept[id] = [0] * 60
  elif "falls asleep" in line :
    start = int(re.findall(r"\d:(\d+)", line)[0])
  else :
    end = int(re.findall(r"\d:(\d+)", line)[0])
    for i in range(start, end):
      slept[id][i] += 1

infos = []
for id in slept :
    infos.append((id, max(slept[id]), slept[id].index(max(slept[id]))))

res = max(infos, key=lambda item:item[1])
print(res)
print(res[0] * res[2])

# max(lis,key=lambda item:item[1])
# tot_slept = { id: sum(slept[id]) for id in slept }
# id = max(tot_slept, key=tot_slept.get)
# min = slept[id].index(max(slept[id]))
# print("id:" + str(id), "min:" + str(min))
# print("res:" + str(id*min))
