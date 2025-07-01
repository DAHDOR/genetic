from math import sin, cos, pi

def a(x: float) -> float:
    if abs(x) < 1e-10:
        return 0.0
    return sin(x)**2 / x

def b(x: float, y: float) -> float:
    return 20 + x - 10 * cos(2 * pi * x) + y - 10 * cos(2 * pi * y)