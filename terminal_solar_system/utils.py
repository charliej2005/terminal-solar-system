import math
import readchar


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


def listen_for_quit(stop_event):
    """Listens for 'q' key input and sets flag to true if detected.

    Args:
        stop_event (Event): The event for which the flag is set.

    Returns:
        None
    """
    while not stop_event.is_set():
        if readchar.readkey() == 'q':
            stop_event.set()
