from functools import reduce
from collections import defaultdict
with open('input15.txt', 'r') as f:
    ws = f.readline().split(',')

hasher = lambda word: reduce(lambda a, b: (a+b)*17, list(map(ord, word)), 0)%256

# part 1
print(sum(hasher(w) for w in ws))

# part 2
boxes = defaultdict(dict)
for w in ws:
    if '=' == w[-2]:
        label, lens = w[:-2], w[-1]
        box = hasher(label)
        boxes[box][label] = int(lens)
    else:
        label = w[:-1]
        box = hasher(label)
        boxes[box].pop(label, None)

print(sum((k+1)*(i+1)*lens for k, v in boxes.items() for i, lens in enumerate(v.values())))
