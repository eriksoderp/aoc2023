import re
from itertools import combinations
from sympy.solvers import solve
from sympy import Symbol
cvs = [[int(i) for i in re.findall(r'-?\d+', l)]
               for l in open('input24.txt', 'r').readlines()]

# part 1
count = 0
bot, top = 200000000000000, 400000000000000
for a, b in combinations(cvs, 2):
    ax, ay, az, avx, avy, avz = a
    bx, by, bz, bvx, bvy, bvz = b
    ak, bk = avy/avx, bvy/bvx
    if ak == bk: continue
    am = ay - (ax*ak)
    bm = by - (bx*bk)
    x = (bm-am)/(ak-bk)
    if (x-ax)*avx < 0 or (x-bx)*bvx < 0: continue
    y = ak*x + am
    if bot <= x <= top and bot <= y <= top:
        count += 1
print(count)

# part 2
x, y, z = Symbol('x'), Symbol('y'), Symbol('z')
vx, vy, vz = Symbol('vx'), Symbol('vy'), Symbol('vz')

ax, ay, az, avx, avy, avz = cvs[0]
bx, by, bz, bvx, bvy, bvz = cvs[1]
cx, cy, cz, cvx, cvy, cvz = cvs[2]

sols = solve([(y-ay)*(avx-vx)-(avy-vy)*(x-ax),
              (z-az)*(avy-vy)-(avz-vz)*(y-ay),
              (y-by)*(bvx-vx)-(bvy-vy)*(x-bx),
              (z-bz)*(bvy-vy)-(bvz-vz)*(y-by),
              (y-cy)*(cvx-vx)-(cvy-vy)*(x-cx),
              (z-cz)*(cvy-vy)-(cvz-vz)*(y-cy)],
              [x, y, z, vx, vy, vz])
print(sum(val for var, val in sols[0].items() if var in [x,y,z]))
