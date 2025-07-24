import math
import random

from terminal_solar_system.config import (
    DEPTH_OF_FIELD_MODIFIER,
    RING_CHAR,
    RING_SIZE_MODIFIER,
)


def render_frame(planets, stars, console, print_color, terminal_x_scale):
    """Returns a rendered frame to be printed.

    Args:
        planets (list[Planet]): List of planets to be drawn.
        stars (list[Star]): List of stars to be drawn.
        console (Console): Console being drawn to.
        print_color (bool): Whether or not to color output.
        terminal_x_scale (float): Font height/width ratio.


    Returns:
        str: Buffer contents rendered to a string.
    """
    width = console.width
    height = console.height
    buffer = [[(' ', None) for _ in range(width)] for _ in range(height)]
    center_x = width // 2
    center_y = height // 2
    sorted_planets = sorted(planets, key=lambda planet: planet.z)
    for star in stars:
        render_star(buffer, star)
    for planet in sorted_planets:
        render_planet(
            buffer,
            planet,
            center_x + planet.x,
            center_y + planet.y,
            terminal_x_scale
        )
    if print_color:
        return "\n".join(
            "".join(
                f"[{color}]{symbol}[/{color}]" if color else symbol
                for symbol, color in row
            )
            for row in buffer
        )
    return "\n".join(
        "".join(
            f"[{'white'}]{symbol}[/{'white'}]" if color else symbol
            for symbol, color in row
        )
        for row in buffer
    )


def render_planet(
        buffer,
        planet,
        center_x,
        center_y,
        terminal_x_scale
):
    """Writes a planet to the buffer for rendering.

    Args:
        buffer (list[list[str]]): Buffer to write to.
        planet (Planet): The planet being drawn.
        center_x (int): Center x-coordinate of the buffer.
        center_y (int): Center y-coordinate of the buffer.
        terminal_x_scale (float): height/width ratio of text in terminal.

    Returns:
        None
    """
    if terminal_x_scale == 0:
        return

    height = len(buffer)
    width = len(buffer[0])

    pixel_written = False
    min_dist = float("inf")

    depth_of_field = planet.z / DEPTH_OF_FIELD_MODIFIER
    inner_radius = planet.radius + depth_of_field - planet.line_width / 2
    outer_radius = planet.radius + depth_of_field + planet.line_width / 2

    for yi in range(height):
        for xi in range(width):
            dx = (xi - center_x) / terminal_x_scale
            dy = (yi - center_y)
            dist = math.sqrt(dx ** 2 + dy ** 2)

            if inner_radius < dist < outer_radius:
                buffer[yi][xi] = (planet.symbol, planet.color)
                pixel_written = True

            if dist < inner_radius:
                buffer[yi][xi] = (planet.fill, planet.color)

            if dist < min_dist:
                min_dist = dist
                min_coords = (yi, xi)

    if not pixel_written:
        yi, xi = min_coords
        if 0 < yi < height - 1 and 0 < xi < width - 1:
            buffer[yi][xi] = (planet.symbol, planet.color)

    if planet.has_ring:
        render_planet_ring(
            buffer,
            planet,
            center_x,
            center_y,
            terminal_x_scale
        )


def render_planet_ring(
    buffer,
    planet,
    center_x,
    center_y,
    terminal_x_scale
):
    """Draws a Planet's ring to the buffer.

    Args:
        buffer (list[list[str]]): Buffer to write to.
        planet (Planet): The planet whose ring is being drawn.
        center_x (int): Center x-coordinate of the buffer.
        center_y (int): Center y-coordinate of the buffer.
        terminal_x_scale (float): height/width ratio of text in terminal.

    Returns:
        None
    """
    height = len(buffer)
    width = len(buffer[0])

    depth_of_field = planet.z / DEPTH_OF_FIELD_MODIFIER
    ring_length = int((planet.radius + depth_of_field) * RING_SIZE_MODIFIER)

    for offset in range(-ring_length, ring_length + 1):
        y = int(center_y + offset)
        x = int(center_x + offset * terminal_x_scale)
        if 0 <= y < height and 0 <= x < width:
            buffer[y][x] = (RING_CHAR, planet.color)


def render_star(buffer, star):
    """Draws a Star to the buffer for rendering.

    Args:
        buffer (list[list[str]]): Buffer to write to.
        star (Star): The star being drawn.

    Returns:
        None
    """
    if (
        star.idx == 0
        or star.y > len(buffer) - 1
        or star.x > len(buffer[0]) - 1
    ):
        star.x = random.randint(0, len(buffer[0]) - 1)
        star.y = random.randint(0, len(buffer) - 1)
    buffer[star.y][star.x] = (star.frames[star.idx], star.color)
