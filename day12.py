import re
from functools import cache

with open('input12.txt', 'r') as f: lines = f.readlines()

parse = lambda line: (line.split()[0], [int(i) for i in re.findall(r'\d+', line)])

@cache
def dp(s, gs, current_size):
    if not s:
        if not gs and current_size == 0: return 1
        elif len(gs) == 1 and current_size == gs[0]: return 1
        else: return 0

    if gs and current_size > gs[0]:
        return 0
    elif not gs and current_size > 0:
        return 0

    count = 0
    current_spring = s[0]
    if current_spring in ['?', '#']:
        count += dp(s[1:], gs, current_size+1)

    if current_spring in ['?', '.']:
        if gs and gs[0] == current_size:
            count += dp(s[1:], gs[1:], 0)
        elif current_size == 0:
            count += dp(s[1:], gs, 0)

    return count

lines = [parse(line) for line in lines]
# part 1
print(sum(dp(s, tuple(gs), 0) for s, gs in lines))

# part 2
lines = [('?'.join([s] * 5), gs * 5) for s, gs in lines]
print(sum(dp(s, tuple(gs), 0) for s, gs in lines))
