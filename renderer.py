import math
from config import TERMINAL_X_SCALE


def render_frame(width, height):
    """Returns a rendered frame to be printed.

    Args:
        width (int): Screen width.
        height (int): Screen height.

    Returns:
        _type_: _description_
    """
    buffer = [[' ' for _ in range(width)] for _ in range(height)]
    center_x = width // 2
    center_y = height // 2
    # Example:
    render_circle(buffer, center_x, center_y, 10, 3)
    return "\n".join("".join(row) for row in buffer)


def render_circle(buffer, center_x, center_y, radius, line_width):
    # TODO: Adjust logic to render a planet, not just a generic circle
    """Writes a circle to the buffer for rendering.

    Args:
        buffer (list[list[str]]): Buffer to write to.
        center_x (int): Center x-coordinate of the buffer.
        center_y (int): Center y-coordinate of the buffer.
        radius (int): Radius of the circle.
        line_width (int): Width of the circle's border.
    """
    height = len(buffer)
    width = len(buffer[0])
    for yi in range(height):
        for xi in range(width):
            dx = (xi - center_x) / TERMINAL_X_SCALE
            dy = (yi - center_y)
            dist = math.sqrt(
                dx ** 2 + dy ** 2
            )
            if (
                dist > radius - line_width / 2
                and dist < radius + line_width / 2
            ):
                buffer[yi][xi] = '*'
