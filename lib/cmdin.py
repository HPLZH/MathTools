import sys
from sympy.abc import *
from sympy import *

__in = [] if sys.stdin.isatty() else [s.strip() for s in sys.stdin.readlines()]
__arg = sys.argv[1:]

rin = __in[:]
rarg = __arg[:]

__patterns: list = []
pattern: list = None

inputs = []
args = []


def __d(p: list):
    global inputs, args, pattern
    inputs = []
    args = []
    if len(p)==0:
        pattern = p[:]
        inputs = __in[:] + __arg[:]
        return True
    for i in range(-1, -len(p)-1, -1):
        try:
            if p[i] == str:
                args.insert(0, __arg[i])
                continue
            if ISkipEval in p[i].mro():
                __r = __arg[i]
            else:
                __r = eval(__arg[i])
            if p[i]!=object:
                __r = p[i](__r)
            args.insert(0, __r)
            pass
        except:
            return False
    pattern = p[:]
    inputs = __in[:] + __arg[:-len(p)]
    return True


def __ds():
    global __patterns, pattern, inputs, args
    __patterns = sorted(__patterns, key=len, reverse=True)
    for p1 in __patterns:
        if __d(p1):
            break
    else:
        inputs = __in[:]+__arg[:]
        args = []
        pattern = None

def set_patterns(*patterns):
    global __patterns
    __patterns = list(patterns)
    __ds()

def add_patterns(*patterns):
    global __patterns
    __patterns += list(patterns)
    __ds()

class ISkipEval:
    pass