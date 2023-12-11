with open('input11.txt', 'r') as f:
    universe = f.readlines()

def get_empty(universe):
    empty = set()
    for i, row in enumerate(universe):
        if row.count('#') == 0: empty.add(i)
    return empty

empty_rows = get_empty(universe)
empty_cols = get_empty([list(i) for i in zip(*universe)])

def distance(a, b, x, y, expander):
    func = lambda l, min, max: len(list(filter(lambda x: min < x and x < max, l)))
    extra_rows = func(empty_rows, min(a, x), max(a, x))*expander
    extra_cols = func(empty_cols, min(b, y), max(b, y))*expander
    return abs(a-x)+abs(b-y) + extra_rows + extra_cols

galaxies = [(i, j) for i, row in enumerate(universe) for j, col in enumerate(row) if col == '#']
galaxy_pairs = [(p1, p2) for i, p1 in enumerate(galaxies) for j, p2 in enumerate(galaxies) if p1 != p2 and i < j]

# part 1
print(sum([distance(*g1, *g2, 1) for g1, g2 in galaxy_pairs]))

# part 2
print(sum([distance(*g1, *g2, 999999) for g1, g2 in galaxy_pairs]))
