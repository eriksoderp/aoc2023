import re
from itertools import groupby
from functools import reduce

with open('input5.txt', 'r') as f:
    lines = f.readlines()

def get_ints(line):
    return list(map(int, re.findall(r'\d+', line)))

def build_map(group):
    dsrs = map(get_ints, group)
    new_map = {range(s, s+r) : d - s for d, s, r in dsrs}
    maps.append(new_map)

maps = []
groups = groupby(lines[2:], lambda x: x == '\n')
list(map(build_map, [list(group)[1:] for key, group in groups if not key]))

# part 1
seeds = get_ints(lines[0])

def get_seed_value(key):
    key = reduce()
    for m in maps:
        for k, v in m.items():
            if key in k:
                key += v
                break
    return key

print(min(map(get_seed_value, seeds)))

# part 2
func = lambda xy: range(xy[0], xy[0]+xy[1])
seeds = list(map(func, list(zip(*[iter(seeds)]*2))))

def range_intersection(source, seed):
    start = max(source.start, seed.start)
    stop = min(source.stop, seed.stop)
    if start < stop:
       return range(start, stop)
    else: return None

def apply_map(seeds, m):
    new_seeds = []
    for seed in seeds:
        for source, offset in m.items():
            intersection = range_intersection(source, seed)
            if intersection:
                new_seeds.append(range(intersection.start + offset,
                                       intersection.stop + offset))
                if seed.start < intersection.start:
                    seeds.append(range(seed.start, intersection.start))
                if seed.stop > intersection.stop:
                    seeds.append(range(intersection.stop, seed.stop))
    return new_seeds

func = lambda r: r.start
print(min(map(func, reduce(apply_map, maps, seeds))))
