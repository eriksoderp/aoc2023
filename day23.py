from copy import deepcopy
import sys
import networkx as nx
sys.setrecursionlimit(10000)
grid = {(j, i):val for i, row in enumerate(open('input23.txt', 'r').readlines())
                   for j, val in enumerate(row.strip()) if val != '#'}

add = lambda x, y, dir_x, dir_y: (x+dir_x, y+dir_y)
turn = lambda dir_x, dir_y: ((dir_y, dir_x), (-dir_y, -dir_x))

start, end = list(grid.keys())[0], list(grid.keys())[-1]

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

        if grid[pos] in '<^>v':
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
path(set(), start, (0, 1))
print(max(results)-1)

# part 2
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
neighbours = {p: [add(*p, *d) for d in dirs if add(*p, *d) in grid] for p in grid}

G = nx.Graph()
G.add_edges_from(((p, n) for p, ns in neighbours.items() for n in ns))

crossways = {p for p, ns in neighbours.items() if len(ns) >= 3}

cws = {n: set(nx.neighbors(G, n)) for n in crossways}
cws[start], cws[end] = set(nx.neighbors(G, start)), set(nx.neighbors(G, end))

G.remove_nodes_from(crossways)
components = list(nx.connected_components(G))

H = nx.Graph()
for c in components:
    u, v = [cw for cw, ns in cws.items() if len(ns.intersection(c)) == 1]
    H.add_edge(u, v, weight=len(c)+1)

max_path = max((sum(H.get_edge_data(u, v)['weight'] for u, v in zip(path, path[1:]))-2 for path in list(nx.all_simple_paths(H, start, end))))

print(max_path)
