import re

metadatas = []

def parse_data() :
    input = open("./input.txt").readline().strip()
    data = [int(x) for x in input.split()]
    return data

def read_node(data) :
    n_child = data[0]
    n_meta = data[1]
    del data[:2]
    for i in range(n_child) :
        read_node(data)
    for i in range(n_meta) :
        metadatas.append(data[i])
    del data[:n_meta]

data = parse_data()

read_node(data)
print(sum(metadatas))
