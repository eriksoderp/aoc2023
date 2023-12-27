from copy import deepcopy
import sys
import networkx as nx
from itertools import combinations
sys.setrecursionlimit(10000)
grid = {(j, i):val for i, row in enumerate(open('input23.txt', 'r').readlines())
                   for j, val in enumerate(row.strip()) if val != '#'}

add = lambda x, y, dir_x, dir_y: (x+dir_x, y+dir_y)
turn = lambda dir_x, dir_y: ((dir_y, dir_x), (-dir_y, -dir_x))

start = list(grid.keys())[0]
end = list(grid.keys())[-1]

def arrow_dir(arrow):
    match arrow:
        case '<': return (-1, 0)
        case '^': return (0, -1)
        case '>': return (1, 0)
        case 'v': return (0, 1)

results = []
def path(visited, pos, dir):
    while pos not in visited:
        if pos not in grid: return -1

        visited.add(pos)
        if pos == end: return len(visited)

        if part1 and grid[pos] in '<^>v':
            dir = arrow_dir(grid[pos])
            pos = add(*pos, *dir)
        else:
            for new_dir in turn(*dir):
                new_pos = add(*pos, *new_dir)
                if new_pos in grid:
                    new_visited = deepcopy(visited)
                    results.append(path(new_visited, new_pos, new_dir))
            pos = add(*pos, *dir)
    return -1

# part 1
part1 = True
path(set(), start, (0, 1))
print(max(results)-1)
# part 2
part1 = False
path(set(), start, (0, 1))
print(max(results)-1)
