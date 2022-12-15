from sympy.abc import *
from sympy import *
import logging
import lib.cmdin
sx = False
_a, _b = -1, 1
if len(lib.cmdin.rin) == 0:
    lib.cmdin.set_patterns([str, object, object], [str])
    if len(lib.cmdin.args) == 2:
        sx = True
else:
    lib.cmdin.set_patterns([object, object], [])
    if len(lib.cmdin.args) == 2:
        sx = True
if sx:
    lib.cmdin.set_patterns([object, object])
    _a, _b = lib.cmdin.args
else:
    lib.cmdin.set_patterns([])

fs = lib.cmdin.inputs
fxs = []
for _f in fs:
    try:
        fx = sympify(_f)
    except Exception as _e:
        logging.error(_e)
    else:
        fxs.append(fx)
        print(fx)

if sx:
    fxs.append((x, _a, _b))

plot(*fxs)
