import re
import itertools
from math import lcm

with open('input8.txt', 'r') as f:
    lines = f.readlines()

words = lambda line: re.findall(r'[A-Z]+', line)
transitions = {node:(left, right) for node, left, right in map(words, lines[2:])}
instructions = [0 if c == 'L' else 1 for c in lines[0].strip()]

def rounds_steps(node, stop_condition):
    steps = 0
    while not stop_condition(node):
        lr = instructions[steps % len(instructions)]
        node = transitions[node][lr]
        steps += 1
    return steps, steps // len(instructions)

# part 1
print(rounds_steps('AAA', lambda node: node == 'ZZZ')[0])

# part 2
ends_with_a = list(filter(lambda node: node.endswith('A'), transitions.keys()))
z_funcs = itertools.repeat(lambda node: node.endswith('Z'), len(ends_with_a))
res = list(map(rounds_steps, ends_with_a, z_funcs))
print(lcm(*list(map(lambda x: int(x[1]), res)))*len(instructions))
