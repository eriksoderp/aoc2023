from itertools import groupby
import re
from copy import deepcopy
from math import prod

lines = [line.strip() for line in open('input19.txt', 'r').readlines()]

gs = [list(g) for k, g in groupby(lines, lambda x: x == '') if not k]

rules = {id:rs.split(',') for irs in gs[0]
                          for id, rs in [re.split(r'[{}]', irs)[:-1]]}

tests = [{v[0]:int(v[2:]) for v in vs[1:-1].split(',')}
                          for vs in gs[1]]

# part 1
def run(t, count, state):
    x, m, a, s = t['x'], t['m'], t['a'], t['s']
    while state not in ('A', 'R'):
        rs = rules[state]
        for r in rs:
            if ':' not in r:
                state = r
                break

            cond, new_state = r.split(':')
            if eval(cond):
                state = new_state
                break

    if state == 'A': count += (x+m+a+s)
    return count

print(sum(run(t, 0, 'in') for t in tests))

# part 2
def all_combinations(sr, count, state):
    todo = [({'x':sr, 'm':sr, 'a':sr, 's':sr}, state)]
    while todo:
        mapping, state = todo.pop()
        if state == 'A':
            count += prod(len(r) for r in mapping.values())
            continue

        if state == 'R': continue

        rs = rules[state]
        for r in rs:
            if ':' not in r:
                todo.append((mapping, r))
                break

            cond, new_state = r.split(':')
            id, ran, n = cond[0], mapping[cond[0]], int(cond[2:])
            new_mapping = deepcopy(mapping)
            if cond[1] == '<':
                low_range = range(ran.start, n)
                new_mapping[id] = low_range
                ran = range(n, ran.stop)
                mapping[id] = ran
            elif cond[1] == '>':
                high_range = range(n+1, ran.stop)
                new_mapping[id] = high_range
                ran = range(ran.start, n+1)
                mapping[id] = ran

            todo.append((new_mapping, new_state))

    return count

print(all_combinations(range(1, 4001), 0, 'in'))
