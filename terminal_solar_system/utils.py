import math


def polar_to_cartesian(radius, theta, phi):
    x = radius * math.cos(theta)
    y = radius * math.sin(theta) * math.sin(phi)
    z = radius * math.sin(theta) * math.cos(phi)
    return x, y, z
