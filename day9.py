import re
from functools import reduce

with open('input9.txt', 'r') as f:
    lines = f.readlines()

get_ints = lambda line: list(map(int, re.findall(r'-?\d+', line)))
histories = list(map(get_ints, lines))

def left_rights(history):
    lefts, rights = 0, 0
    sign = 1
    while not set(history) == {0}:
        lefts += sign * history[0]
        rights += history[-1]
        history = [num2 - num1 for num1, num2 in zip(history, history[1:])]
        sign *= -1

    return lefts, rights

sumf = lambda lr, current: (lr[0]+current[0], lr[1]+current[1])

# left value part 2, right value part 1
print(list(reduce(sumf, list(map(left_rights, histories)), (0, 0))))
