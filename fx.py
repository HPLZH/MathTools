from sympy.abc import *
from sympy import *
import lib.cmdin
lib.cmdin.set_patterns([object])

x0 = lib.cmdin.args[0]

fs = lib.cmdin.inputs
for _f in fs:
    try:
        fx = sympify(_f)
        fx = fx.subs(x, x0)
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(fx)
