file = open("./input")
data = [line.strip() for line in file.readlines()]

def id_difference(id1, id2) :
    diff = 0
    for i, char in enumerate(id1) :
        if char != id2[i] :
            diff += 1
    return diff

def common_char(id1, id2) :
    common = ""
    for i, char in enumerate(id1) :
        if char == id2[i] :
            common += char
    return common

# possible improvements

# use zip(id1, id2)

# def part2(box_ids: Iterable[str]) -> str:
# 	matching_pair = next(t for t in combinations(box_ids, 2) if is_correct_pair(*t))
# 	return matching_letters(*matching_pair)
