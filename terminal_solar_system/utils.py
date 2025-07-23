import math


def polar_to_cartesian(radius: float, theta: float, phi: float):
    """Converts polar coordinates to cartesian coordinates with inclination.

    Args:
        radius (float): Radius on polar plane.
        theta (float): Angle of revolution in radians.
        phi (float): Angle of inclination in radians.

    Returns:
        tuple: (x, y, z) cartesian coordinates.
    """
    x = radius * math.cos(theta)
    y = radius * math.sin(theta) * math.sin(phi)
    z = radius * math.sin(theta) * math.cos(phi)
    return x, y, z
