from sympy.abc import *
from sympy import *
import lib.cmdin

lib.cmdin.set_patterns([])

matss = lib.cmdin.inputs

for mats in matss:
    try:
        mat = eval(mats)
        detr = mat.det()
    except Exception as _e:
        print("ERROR")
        print(_e, file=lib.cmdin.sys.stderr)
    else:
        print(detr)
