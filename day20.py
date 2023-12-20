import re
from math import lcm

destinations, types, state, conjunctions = {}, {}, {}, {}

for s in open('input20.txt', 'r').readlines():
    key = re.findall(r'(&?%?\w+)\s*->', s)[0]
    values = [c.strip() for c in re.findall(r'->\s*(.*)', s)[0].split(',')]

    if key != 'broadcaster':
        types[key[1:]] = key[0]
        key = key[1:]
    else:
        types[key] = key

    state[key] = -1
    destinations[key] = values

for k, t in types.items():
    conjunctions[k] = {i:-1 for i, ds in destinations.items() if t == '&' and k in ds}

def run(todo, i):
    hi, lo = 0, 0
    while todo:
        key, last_key, pulse = todo.pop(0)
        if pulse == 1: hi += 1
        else: lo += 1

        if key not in types.keys(): continue

        type = types[key]
        if type == '%':
            if pulse == 1: continue
            pulse *= state[key]
            state[key] = pulse
        elif type == '&':
            conjunctions[key][last_key] = pulse
            pulse = -1 if all(map(lambda p: p == 1, conjunctions[key].values())) else 1
            if pulse == 1 and key in conjunctions[rx_parent].keys():
                cycles[key].append(i)

        for d in destinations[key]:
            todo.append((d, key, pulse))

    return hi, lo

hi, lo = 0, 0
i = 0
rx_parent = [p for p, ds in destinations.items() if 'rx' in ds][0]
cycles = {p:[] for p in conjunctions[rx_parent]}
while not all(map(lambda l: len(l) >= 2, cycles.values())):
    i += 1
    h, l = run([('broadcaster', 'button', -1)], i)
    if i <= 1000:
        hi, lo = hi+h, lo+l

# part 1
print(hi*lo)

# part 2
print(lcm(*(l[1]-l[0] for l in cycles.values())))
