from sympy.abc import *
from sympy import *
import lib.cmdin

inlines = lib.cmdin.rin

_r = []
cur = []

for line in inlines:
    xs = line.strip().split(",")
    while len(xs) > 0 and xs[-1].strip() == "":
        xs.pop()
    for i in range(len(xs)):
        if xs[i].strip() == "":
            xs[i] = "0"
    if len(xs) == 0:
        if len(cur) == 0:
            pass
        else:
            _r.append(Matrix(cur))
            cur = []
    else:
        if len(cur) != 0 and len(xs) != len(cur[0]):
            _r.append(Matrix(cur))
            cur = []
        cur.append(xs)
if len(cur) != 0:
    _r.append(Matrix(cur))
    cur = []
for _m in _r:
    print(_m)
