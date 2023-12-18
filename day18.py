from shapely import Polygon

def get_dir(dir):
    match dir:
        case 'R': return (1, 0)
        case 'L': return (-1, 0)
        case 'D': return (0, 1)
        case 'U': return (0, -1)

def get_area(instructions):
    path, point = [], (0, 0)
    for d, l, _ in instructions:
        dir = get_dir(d)
        point = add(*point, *scale(*dir, int(l)))
        path.append(point)
    poly = Polygon(path)
    return int(poly.area + poly.length/2 + 1)

# part 1
instructions = [tuple(l.split()) for l in open('input18.txt').readlines()]
print(get_area(instructions))

# part 2
def get_hexa_dir(c):
    match c:
        case '0': return 'R'
        case '1': return 'D'
        case '2': return 'L'
        case '3': return 'U'

parse_color = lambda color: (get_hexa_dir(color[-2]), int(color[2:-2], 16), color)
instructions = [parse_color(c) for _, _, c in instructions]
print(get_area(instructions))
