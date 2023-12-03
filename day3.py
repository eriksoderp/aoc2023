import re
from collections import defaultdict
import math

with open('input3.txt', 'r') as f:
    grid = f.readlines()

numbers = []
symbols = {}

for i, line in enumerate(grid):
    arr = [(i, match) for match in re.finditer(r'\d+', line)]
    numbers.extend(arr)
    for j, char in enumerate(line):
        if not char.isdigit() and char != '.' and char != '\n':
            symbols[(i,j)] = char

# part 1
def is_part_number(number):
    row, reg = number
    for i in [row-1, row, row+1]:
        for j in range(reg.start()-1, reg.end()+1):
            if (i, j) in symbols:
                return True

    return False

func = lambda number: int(number[1].group())
print(sum(map(func, filter(is_part_number, numbers))))

# part 2
gears = defaultdict(list)

def maybe_add_part_gear(number):
    row, reg = number
    for i in range(row-1, row+2):
        for j in range(reg.start()-1, reg.end()+1):
            if (i,j) in symbols and symbols[(i,j)] == '*':
                gears[(i,j)].append(int(reg.group()))

list(map(maybe_add_part_gear, numbers))
func = lambda gear: math.prod(gear) if len(gear) == 2 else 0
print(sum(map(func, gears.values())))
