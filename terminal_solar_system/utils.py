import math


def polar_to_cartesian(radius, theta):
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    return x, y
