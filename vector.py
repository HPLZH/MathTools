from sympy.abc import *
from sympy import *
import lib.cmdin

inlines = lib.cmdin.rin

_r = []

for line in inlines:
    xs = line.strip().split(",")
    while len(xs) > 0 and xs[-1].strip() == "":
        xs.pop()
    for i in range(len(xs)):
        if xs[i].strip() == "":
            xs[i] = "0"
    if len(xs) == 0:
        pass
    else:
        _r.append(Matrix(xs))
for _m in _r:
    print(_m)
