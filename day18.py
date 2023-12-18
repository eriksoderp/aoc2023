from shapely import Polygon
from itertools import accumulate

def get_dir(dir):
    match dir:
        case 'R' | '0': return (1, 0)
        case 'D' | '1': return (0, 1)
        case 'L' | '2': return (-1, 0)
        case 'U' | '3': return (0, -1)

def get_area(instructions):
    poly =  Polygon(accumulate([(*get_dir(d), int(l)) for d, l, _ in instructions], \
                    lambda p, i: (p[0]+i[0]*i[2], p[1]+i[1]*i[2]), initial=(0, 0)))
    return int(poly.area + poly.length/2 + 1)

# part 1
instructions = [tuple(l.split()) for l in open('input18.txt').readlines()]
print(get_area(instructions))

# part 2
instructions = [(c[-2], int(c[2:-2], 16), c) for _, _, c in instructions]
print(get_area(instructions))
