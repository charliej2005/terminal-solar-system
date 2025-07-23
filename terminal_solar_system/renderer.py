import math
from config import TERMINAL_X_SCALE


def render_frame(planets, width, height):
    """Returns a rendered frame to be printed.

    Args:
        planets (list[Planet]): List of planets to be drawn.
        width (int): Screen width.
        height (int): Screen height.

    Returns:
        str: Buffer contents rendered to a string.
    """
    buffer = [[' ' for _ in range(width)] for _ in range(height)]
    center_x = width // 2
    center_y = height // 2
    for planet in planets:
        render_planet(buffer, planet, center_x + planet.x, center_y + planet.y)
    return "\n".join("".join(row) for row in buffer)


def render_planet(
        buffer,
        planet,
        center_x,
        center_y,
):
    """Writes a planet to the buffer for rendering.

    Args:
        buffer (list[list[str]]): Buffer to write to.
        planet (Planet): The planet being drawn.
        center_x (int): Center x-coordinate of the buffer.
        center_y (int): Center y-coordinate of the buffer.
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
                dist > planet.radius - planet.line_width / 2
                and dist < planet.radius + planet.line_width / 2
            ):
                buffer[yi][xi] = planet.symbol
