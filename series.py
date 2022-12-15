from sympy.abc import *
from sympy import *
import lib.cmdin


def int_s(x): return int(str(x))


lib.cmdin.set_patterns([int_s, object], [int_s])

x0 = 0 if len(lib.cmdin.args) == 1 else lib.cmdin.args[1]
_n = lib.cmdin.args[0]+1

fs = lib.cmdin.inputs
for _f in fs:
    try:
        fx = sympify(_f)
        sf = series(fx, x, x0, _n).removeO()
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(sf)
