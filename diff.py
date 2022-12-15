from sympy.abc import *
from sympy import *
import lib.cmdin
sx = False
x0 = 0
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

fs = lib.cmdin.inputs
for _f in fs:
    try:
        fx = sympify(_f)
        df = diff(fx, x)
        if sx:
            df = df.subs(x, x0)
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(df)
