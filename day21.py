import numpy as np
grid = {(j, i):v for i, row in enumerate(open('input21.txt', 'r').readlines())
                 for j, v in enumerate(row.strip())}

starting_position = [pos for pos, v in grid.items() if v == 'S'][0]
width, height = list(grid.keys())[-1]
width, height = width+1, height+1

def take_steps(todo, steps):
    stop = width // 2 + 2 * width
    while steps < stop:
        new_todo = set()
        for j, i in todo:
            for x, y in ((j-1, i), (j+1, i), (j, i-1), (j, i+1)):
                mod_x, mod_y =  x % width, y % height
                if grid[(mod_x, mod_y)] != '#':
                    new_todo.add((x, y))

        steps += 1
        if steps == 64:
            # part 1
            print(len(new_todo))
        if (steps - 65) % 131 == 0:
            lens.append(len(new_todo))
        todo = new_todo

    return todo

todo = set()
todo.add(starting_position)
lens = []
take_steps(todo, 0)

# part 2
def solve_quadratic(p1, p2, p3):
    A = np.array([[p1[0]**2, p1[0], 1], [p2[0]**2, p2[0], 1], [p3[0]**2, p3[0], 1]])
    B = np.array([p1[1], p2[1], p3[1]])

    a, b, c = np.linalg.solve(A, B)

    return a, b, c

points = ((x, y) for x, y in zip(range(3), lens))
a, b, c = solve_quadratic(*points)
x = 26501365//width
print(int(a*x**2 + b*x + c))
