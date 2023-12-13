from itertools import groupby
import re
import editdistance
with open('input13.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

groups = groupby(lines, lambda x: x == '')
groups = [list(g) for k, g in groups if not k]
transpose = lambda lines: [''.join(i) for i in zip(*lines)]

def difference(g1, g2, differences):
    if len(g1) > len(g2) or len(g2) > len(g1):
        return False

    difference = 0
    for l1, l2 in zip(g1, g2):
        if l1 == l2: continue
        ed = editdistance.eval(l1, l2)
        if ed > 1: return False
        else: difference += ed

    if difference == differences:
        return True
    return False

def func(group, differences):
    g = len(group)-1
    for i in range(g):
        if difference(group[0:i+1], group[2*i+1:i:-1], differences):
            return i+1
        if difference(group[g-1-2*i:g-i], group[g:g-1-i:-1], differences):
            return g-i
    return 0

def solve(group, differences):
    res = func(group, differences)*100
    if res == 0:
        group = transpose(group)
        res = func(group, differences)
    return res

# part 1
print(sum(solve(g, 0) for g in groups))

# part 2
print(sum(solve(g, 1) for g in groups))
