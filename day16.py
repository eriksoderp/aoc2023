import queue
with open('input16.txt', 'r') as f:
    grid = list(map(str.strip, f.readlines()))

is_in_grid = lambda x, y: 0 <= y < len(grid) and 0 <= x < len(grid[0])

def reflect(c, dir_x, dir_y):
    if c == '/': return (-1*dir_y, -1*dir_x)
    if c == '\\': return (dir_y, dir_x)

def energizer(x, y, direction):
    while is_in_grid(x, y):
        energized.add((x,y))
        c = grid[y][x]

        if c == '|' and direction[0] != 0:
            n, s = (0, -1), (0, 1)
            return [(x, y-1, n), (x, y+1, s)]
        elif c == '-' and direction[1] != 0:
            w, e = (-1, 0), (1, 0)
            return [(x-1, y, w), (x+1, y, e)]
        elif c in ['\\', '/']:
            direction = reflect(c, *direction)

        x, y = x+direction[0], y+direction[1]

    return None

energized = set()
task_queue = queue.Queue()
memo = set()

def run(init_state):
    task_queue.put(init_state)
    while not task_queue.empty():
        args = task_queue.get()
        result = energizer(*args)
        if result is not None:
            for r in result:
                if r in memo: continue
                memo.add(r)
                task_queue.put(r)

    memo.clear()
    results.append(len(energized))
    energized.clear()
    return None

# part 1
results = []
run((0, 0, (1, 0)))
print(max(results))

# part 2
results = []
glen = len(grid)
innerglen = len(grid[0])
for i in range(glen):
    run((0, i, (1, 0)))
    run((innerglen-1, i, (-1, 0)))
for j in range(innerglen):
    run((j, 0, (0, 1)))
    run((j, glen-1, (0, -1)))
print(max(results))
