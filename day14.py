from collections import defaultdict
from copy import deepcopy

with open('input14.txt', 'r') as f: lines = [list(line.strip()) for line in f.readlines()]

def tilt(matrix):
    cols = defaultdict(int)
    value = len(matrix)
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == '.':
                cols[j] += 1
            elif c == 'O':
                matrix[i][j] = '.'
                matrix[i-cols[j]][j] = c
            elif c == '#':
                cols[j] = 0
    return matrix

def tilt_maybe_rotate(matrix, number):
    matrix = tilt(matrix)
    if number > 0: matrix = rotate(matrix)

    return matrix

def solve(matrix, tilts):
    if tilts == 1: return tilt(matrix)

    s = {}
    for i in range(tilts+1):
        k = ''.join(c for sl in matrix for c in sl)
        matrix = tilt_maybe_rotate(matrix, i)
        if k in s: return solve(matrix, (tilts-i) % (i-s[k]))
        s[k] = i
    return matrix

rotate = lambda matrix: [list(reversed(col)) for col in zip(*matrix)]
value = len(lines)

# part 1
print(sum(l.count('O')*(value-i) for i, l in enumerate(solve(deepcopy(lines), 1))))

# part 2
print(sum(l.count('O')*(value-i) for i, l in enumerate(solve(lines, 4*10**9))))
