from matplotlib.path import Path
with open('input10.txt', 'r') as f:
    matrix = f.readlines()

all_points = []
def all_points_and_start(matrix):
    start = None
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            all_points.append((i, j))
            if col == 'S': start = (i, j)
    return start

def move(rowcol, direction):
    if direction in ['N', 'W']: rowcol -= 1
    else: rowcol += 1

    return rowcol, direction

row, col = all_points_and_start(matrix)
allowed = {'W': ['F', '-', 'L'], 'N': ['7', '|', 'F'], 'E': ['J', '-', '7'], 'S': ['L', '|', 'J']}

for m in ['N', 'E', 'S', 'W']:
    cr, cc = row, col
    if m in ['N', 'S']: cr, _ = move(cr, m)
    else: cc, _ = move(cc, m)
    if matrix[cr][cc] in allowed[m]:
        current_row, current_col, last_move = cr, cc, m
        break

path = [(row, col)]

steps = 1
node = matrix[current_row][current_col]
while not node == 'S':
    path.append((current_row, current_col))
    if node == 'F':
        if last_move == 'N': current_col, last_move = move(current_col, 'E')
        elif last_move == 'W': current_row, last_move = move(current_row, 'S')
    elif node == 'J':
        if last_move == 'E': current_row, last_move = move(current_row, 'N')
        elif last_move == 'S': current_col, last_move = move(current_col, 'W')
    elif node == '-': current_col, last_move = move(current_col, last_move)
    elif node == '7':
        if last_move == 'E': current_row, last_move = move(current_row, 'S')
        elif last_move == 'N': current_col, last_move = move(current_col, 'W')
    elif node == 'L':
        if last_move == 'S': current_col, last_move = move(current_col, 'E')
        elif last_move == 'W': current_row, last_move = move(current_row, 'N')
    elif node == '|': current_row, last_move = move(current_row, last_move)

    steps += 1
    node = matrix[current_row][current_col]

# part 1
furthest = steps // 2 + 1 if steps % 2 == 1 else steps // 2
print(furthest)

# part 2
not_path = list(filter(lambda p: p not in path, all_points))
path = Path(path)
contained = len(list(filter(lambda x: x, path.contains_points(not_path))))
print(contained)
