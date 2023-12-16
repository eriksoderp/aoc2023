import queue
with open('input16.txt', 'r') as f:
    grid = list(map(str.strip, f.readlines()))

is_in_grid = lambda x, y: 0 <= y < len(grid) and 0 <= x < len(grid[0])

def reflect(c, dir_x, dir_y):
    if c == '/': return (-1*dir_y, -1*dir_x)
    if c == '\\': return (dir_y, dir_x)

def energizer(x, y, direction):
    while (x, y, direction) not in memo and is_in_grid(x, y):
        memo.add((x, y, direction))
        energized.add((x,y))
        c = grid[y][x]

        if c == '|' and direction[0] != 0:
            n, direction = (0, -1), (0, 1)
            energizer(x, y-1, n)
        elif c == '-' and direction[1] != 0:
            w, direction = (-1, 0), (1, 0)
            energizer(x-1, y, w)
        elif c in ['\\', '/']:
            direction = reflect(c, *direction)

        x, y = x+direction[0], y+direction[1]

    return None

energized = set()
task_queue = queue.Queue()
memo = set()

def run(init_state):
    energizer(*init_state)
    memo.clear()
    results[init_state] = len(energized)
    energized.clear()
    return None

results = {}
glen = len(grid)
innerglen = len(grid[0])
for i in range(glen):
    run((0, i, (1, 0)))
    run((innerglen-1, i, (-1, 0)))
for j in range(innerglen):
    run((j, 0, (0, 1)))
    run((j, glen-1, (0, -1)))

# part 1
print(results[(0, 0, (1, 0))])
# part 2
print(max(results.values()))
