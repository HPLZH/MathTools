from sympy.abc import *
from sympy import *
import logging
import lib.cmdin
sx = False
_a, _b = -1, 1
lib.cmdin.set_patterns([float, float], [])
if len(lib.cmdin.args) == 2:
    sx = true
    _a, _b = lib.cmdin.args

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
