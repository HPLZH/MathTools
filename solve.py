from sympy.abc import *
from sympy import *
import lib.cmdin
lib.cmdin.set_patterns([])
fx = sympify(lib.cmdin.inputs[0])
eqfx = Eq(fx, 0)
print(*solve(eqfx, x, domain=Reals), sep="\n")
