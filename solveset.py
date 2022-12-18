from sympy.abc import *
from sympy import *
import lib.cmdin
lib.cmdin.set_patterns([])
fs = lib.cmdin.inputs
for _f in fs:
    try:
        fx = sympify(_f)
        eqfx = Eq(fx, 0)
        sset = solveset(eqfx, x)
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(sset)
