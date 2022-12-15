from sympy.abc import *
from sympy import *
import lib.cmdin
lib.cmdin.set_patterns([])

def toNumber(expr):
    _r = expr
    try:
        _r = float(expr)
    except:
        _r = complex(expr)
    return _r

fs = lib.cmdin.inputs
for _f in fs:
    try:
        fx = toNumber(eval(_f))
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(fx)
