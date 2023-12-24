from collections import defaultdict
xyzs = [tuple(line.strip().split('~')) for line in open('input22.txt', 'r').readlines()]

ranges = []
for i, (a, b) in enumerate(xyzs):
    a = map(int, a.split(','))
    b = map(int, b.split(','))
    ranges.append([range(x1, x2+1) for x1, x2 in zip(a, b)])

sort_key = lambda rs: rs[2].start
ranges.sort(key=sort_key)
def intersects(a, b):
    for x in a[0]:
        for y in a[1]:
            if x in b[0] and y in b[1]:
                return True
    return False

parents = defaultdict(set)
for i, rs1 in enumerate(ranges):
    for j, rs2 in enumerate(ranges[i+1:]):
        if intersects(rs1, rs2): parents[i+j+1].add(i)

for i, rs in enumerate(ranges):
    if i not in parents: ranges[i] = [rs[0], rs[1], range(1, rs[2].stop-rs[2].start-1)]

parents = dict(sorted(parents.items()))

children = defaultdict(set)
for j, ps in parents.items():
    maxZ = max(ranges[p][2].stop for p in ps)

    ranges[j][2] = range(maxZ, maxZ+len(ranges[j][2]))
    kept_parents = set()
    for p in ps:
        if ranges[p][2].stop == maxZ:
            kept_parents.add(p)
            children[p].add(j)

    parents[j] = kept_parents

count = len(ranges)
bad = defaultdict(set)
for p, vs in parents.items():
    if len(vs) == 1: bad[vs.pop()].add(p)

# part 1
print(len(ranges) - len(bad))

# part 2
def disintegrate(piece):
    affected = set()
    def falls(piece):
        if piece in affected: return
        affected.add(piece)
        for c in children[piece]:
            if not len(parents[c] - affected):
                falls(c)
    falls(piece)
    return len(affected)

print(sum(disintegrate(piece)-1 for piece in bad))
