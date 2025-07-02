from math import sin, cos, pi

def a(ind: float) -> float:
    x = ind
    if abs(x) < 1e-10:
        return 0.0
    return sin(x)**2 / x

def b(ind: tuple) -> float:
    x, y = ind
    return 20 + x - 10 * cos(2 * pi * x) + y - 10 * cos(2 * pi * y)