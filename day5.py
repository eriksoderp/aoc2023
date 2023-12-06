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

maps = []
start_func = lambda r: r.start
groups = groupby(lines[2:], lambda x: x == '\n')
list(map(build_map, [list(group)[1:] for key, group in groups if not key]))
seeds = get_ints(lines[0])

# part 1
func = lambda seed: range(seed, seed+1)
ranges = list(map(func, seeds))
print(min(map(start_func, reduce(apply_map, maps, ranges))))

# part 2
func = lambda xy: range(xy[0], xy[0]+xy[1])
ranges = list(map(func, list(zip(*[iter(seeds)]*2))))
print(min(map(start_func, reduce(apply_map, maps, ranges))))
