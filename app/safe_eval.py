import math

def safe_eval(expr):
    allowed = {
        k: getattr(math, k) for k in dir(math)
        if not k.startswith("__")
    }
    allowed.update({"abs": abs})
    return eval(expr, {"__builtins__": None}, allowed)