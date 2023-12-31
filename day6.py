import re
from math import prod
import numpy as np

def get_ints(line):
    return list(map(int, re.findall(r'\d+', line)))

with open('input6.txt', 'r') as f:
    lines = f.readlines()

def scores_over(total_time, hi_score):
    roots = np.roots([-1, total_time, -hi_score])
    return total_time - 2*(int(min(roots)) + 1) + 1

# part 1
times, scores = map(get_ints, lines)
func = lambda timescore: scores_over(timescore[0], timescore[1])
print(prod(list(map(func, zip(times, scores)))))

# part 2
func = lambda line: line.replace(" ", "")
times, scores = map(get_ints, list(map(func, lines)))
print(scores_over(times[0], scores[0]))
