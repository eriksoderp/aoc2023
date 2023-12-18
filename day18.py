from shapely import Polygon
def get_dir(dir):
    match dir:
        case 'R' | '0': return (1, 0)
        case 'D' | '1': return (0, 1)
        case 'L' | '2': return (-1, 0)
        case 'U' | '3': return (0, -1)

def get_area(instructions):
    path, point = [], (0, 0)
    for d, l, _ in instructions:
        dx, dy = get_dir(d)
        point = (point[0] + dx*int(l), point[1] + dy*int(l))
        path.append(point)
    poly = Polygon(path)
    return int(poly.area + poly.length/2 + 1)

# part 1
instructions = [tuple(l.split()) for l in open('input18.txt').readlines()]
print(get_area(instructions))

# part 2
parse_color = lambda color: (color[-2], int(color[2:-2], 16), color)
instructions = [parse_color(c) for _, _, c in instructions]
print(get_area(instructions))
