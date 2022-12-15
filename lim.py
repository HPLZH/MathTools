from sympy.abc import *
from sympy import *
import lib.cmdin
lib.cmdin.set_patterns([object, str], [object])

x0 = lib.cmdin.args[0]
_m = "+-" if len(lib.cmdin.args) < 2 else lib.cmdin.args[1]

fs = lib.cmdin.inputs
for f in fs:
    try:
        fx = sympify(f)
        limf = limit(fx, x, x0, _m)
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(limf)
