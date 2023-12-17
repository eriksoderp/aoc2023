from math import inf
from heapq import heappop, heappush
from collections import defaultdict

grid = {(j, i): int(n) for i, row in enumerate(open('input17.txt').readlines())
                       for j, n in enumerate(row.strip())}

add = lambda x, y, dir_x, dir_y: (x+dir_x, y+dir_y)
scale = lambda dir_x, dir_y, scalar: (dir_x*scalar, dir_y*scalar)
turn = lambda dir_x, dir_y: ((-dir_y, -dir_x), (dir_y, dir_x))

def dijkstra(min_steps, max_steps):
    end = list(grid.keys())[-1]
    heats = defaultdict(lambda: inf)
    q = [(0, (0, 0), (0, 1)), (0, (0, 0), (1, 0))]
    while q:
        heat, pos, dir = heappop(q)

        if pos == end: return heat

        if heat > heats[(pos, dir)]: continue

        for new_dir in turn(*dir):
            new_heat = heat
            for d in range(1, max_steps+1):
                new_pos = add(*pos, *scale(*new_dir, d))
                if new_pos in grid:
                    new_heat += grid[new_pos]

                    if d < min_steps: continue

                    k = (new_pos, new_dir)
                    if new_heat < heats[k]:
                        heats[k] = new_heat
                        heappush(q, (new_heat, *k))
    return -1

# part 1
print(dijkstra(1, 3))

# part 2
print(dijkstra(4, 10))
