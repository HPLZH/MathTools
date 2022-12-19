from sympy.abc import *
from sympy import *
import logging
import lib.cmdin
sx = False
_a, _b = -1, 1

class tosep(lib.cmdin.ISkipEval):
    def __init__(self, _s):
        super().__init__()
        if _s != "to":
            raise Exception()

lib.cmdin.set_patterns([object,tosep,object],[])
if len(lib.cmdin.args) == 3:
    sx = True
    _a, _, _b = lib.cmdin.args

fs = lib.cmdin.inputs
for _f in fs:
    try:
        fx = sympify(_f)
        if sx:
            fx = integrate(fx, (x, _a, _b))
        else:
            fx = integrate(fx, x)
            pass
    except Exception as _e:
        logging.error(_e)
    else:
        print(fx)
