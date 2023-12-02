import re
from collections import defaultdict
import math

with open('input2.txt', 'r') as f:
    games = f.readlines()

# part 1
constraints = {'red': 12, 'green': 13, 'blue': 14}

def is_possible_hands(hands):
    items = re.split(r'[;,]\s*', hands)
    for item in items:
        number, color = int(item.split()[0]), item.split()[1]
        if number > constraints[color]:
            return False

    return True

def is_possible_game(game):
    id, hands = game.split(':')
    if is_possible_hands(hands):
        return int(id.split()[1])

    return 0

print(sum(map(is_possible_game, games)))

# part 2
def power_of_game(game):
    hands = game.split(':')[1]
    items = re.split(r'[;,]\s*', hands)
    colors = defaultdict(int)
    for item in items:
        number, color = int(item.split()[0]), item.split()[1]
        if number > colors[color]:
            colors[color] = number

    return math.prod(colors.values())

print(sum(map(power_of_game, games)))
