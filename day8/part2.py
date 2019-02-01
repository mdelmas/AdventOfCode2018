import re

metadatas = []

def parse_data() :
    input = open("./example.txt").readline().strip()
    data = [int(x) for x in input.split()]
    return data

def get_root_value(data, value) :
    print(data)
    n_child = data[0]
    n_meta = data[1]
    print(n_child, n_meta)
    del data[:2]
    if n_child == 0 :
        node_value = sum(data[:n_meta])
        del data[:n_meta]
        return value + node_value
    node_value = 0
    for i in range(n_meta) :
        node_value = get_root_value(data, value)
    return value

data = parse_data()
print(get_root_value(data, 0))
print(data)
# read_node(data)
# print(sum(metadatas))
# for x in data :
#     print(x)
