from sympy.abc import *
from sympy import *
import lib.cmdin
def int_s(_x): return int(str(_x))


sx = False
x0 = 0
_n = 1

lib.cmdin.set_patterns([int_s, object], [int_s])
if lib.cmdin.pattern == None:
    if len(lib.cmdin.rin) == 0:
        lib.cmdin.set_patterns([str, object], [str])
        if len(lib.cmdin.args) == 2:
            sx = True
    else:
        lib.cmdin.set_patterns([object], [])
        if len(lib.cmdin.args) == 1:
            sx = True
    if sx:
        lib.cmdin.set_patterns([object])
        x0 = lib.cmdin.args[0]
    else:
        lib.cmdin.set_patterns([])
    pass
else:
    _n = lib.cmdin.args[0]
    if len(lib.cmdin.args) == 2:
        sx = True
        x0 = lib.cmdin.args[1]

fs = lib.cmdin.inputs
for _f in fs:
    try:
        fx = sympify(_f)
        df = diff(fx, x, _n)
        if sx:
            df = df.subs(x, x0)
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(df)
