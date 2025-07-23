import math

from terminal_solar_system.config import TERMINAL_X_SCALE
from terminal_solar_system.config import DEPTH_OF_FIELD_MODIFIER


def render_frame(planets, width, height):
    """Returns a rendered frame to be printed.

    Args:
        planets (list[Planet]): List of planets to be drawn.
        width (int): Screen width.
        height (int): Screen height.

    Returns:
        str: Buffer contents rendered to a string.
    """
    buffer = [[(' ', None) for _ in range(width)] for _ in range(height)]
    center_x = width // 2
    center_y = height // 2
    sorted_planets = sorted(planets, key=lambda planet: planet.z)
    for planet in sorted_planets:
        render_planet(buffer, planet, center_x + planet.x, center_y + planet.y)
    return "\n".join(
        "".join(
            f"[{color}]{symbol}[/{color}]" if color else symbol
            for symbol, color in row
        )
        for row in buffer
    )


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

    pixel_written = False
    min_dist = float("inf")

    depth_of_field = planet.z / DEPTH_OF_FIELD_MODIFIER
    inner_radius = planet.radius + depth_of_field - planet.line_width / 2
    outer_radius = planet.radius + depth_of_field + planet.line_width / 2

    for yi in range(height):
        for xi in range(width):
            dx = (xi - center_x) / TERMINAL_X_SCALE
            dy = (yi - center_y)
            dist = math.sqrt(dx ** 2 + dy ** 2)

            if inner_radius < dist < outer_radius:
                buffer[yi][xi] = (planet.symbol, planet.color)
                pixel_written = True

            if dist < inner_radius:
                buffer[yi][xi] = (' ', None)

            if dist < min_dist:
                min_dist = dist
                min_coords = (yi, xi)

    if not pixel_written:
        yi, xi = min_coords
        buffer[yi][xi] = (planet.symbol, planet.color)
