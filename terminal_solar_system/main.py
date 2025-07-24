from time import sleep
import random
import threading

from rich.console import Console
from rich.live import Live

from terminal_solar_system.utils import listen_for_quit
from terminal_solar_system.planets import Planet, Star, Sun
from terminal_solar_system.renderer import render_frame
from terminal_solar_system.config import (
    BORDER_SYMBOLS,
    FILL_SYMBOLS,
    INCLINATION_CHANCE,
    MAX_INCLINATION,
    MAX_ORBIT_RADIUS,
    MAX_PERIOD,
    MAX_RADIUS,
    MIN_PERIOD,
    MIN_RADIUS,
    ORBIT_RADIUS_MULTIPLIER,
    PLANET_COLORS,
    RING_CHANCE
)


def main(framerate, print_color, star_count, terminal_x_scale, random_planets):
    """Runs a simple animated ASCII solar system in your Unix terminal.

    Args:
        framerate (int): Frames per second.
        print_color (bool): Enabled color.
        star_count (int): Stars in the background.
        terminal_x_scale (float): Font height/width ratio.
        random_planets (bool): Randomised planets.

    Returns:
        None
    """
    console = Console()
    stars = [Star(console) for _ in range(star_count)]
    planets = []
    if random_planets:
        add_random_solar_system(planets)
    else:
        add_solar_system(planets)

    stop_event = threading.Event()
    threading.Thread(
        target=listen_for_quit,
        args=(stop_event,),
        daemon=True
    ).start()

    with Live("", refresh_per_second=framerate, console=console) as live:
        while not stop_event.is_set():
            for star in stars:
                star.update()
            for planet in planets:
                planet.update()
            live.update(
                render_frame(
                    planets,
                    stars,
                    console,
                    print_color,
                    terminal_x_scale
                )
            )
            sleep(1 / framerate)


def add_solar_system(planets):
    """
    Populates the given list with Planet objects representing the solar system
    using vibrant versions of their real-life colors.

    Args:
        planets (list): The list to which Planet objects will be appended.

    Returns:
        None
    """
    planets.append(
        Sun(10, symbol='☀', fill='`', color='bright_yellow')
    )  # Sun
    planets.append(
        Planet(2, 40, 4.8, symbol='☿', color='bright_white')
    )  # Mercury
    planets.append(
        Planet(3, 50, 7.2, symbol='♀', fill=',', color='bright_yellow')
    )  # Venus
    planets.append(
        Planet(3, 60, 6.0, symbol='⊕', fill='`', color='bright_blue')
    )  # Earth
    planets.append(
        Planet(2, 70, 5.4, symbol='♂', fill='.', color='bright_red')
    )  # Mars
    planets.append(
        Planet(5, 80, 12.0, symbol='♃', fill='\'', color='orange1')
    )  # Jupiter
    planets.append(
        Planet(4, 90, 15.0, symbol='♄', fill=':', color='gold1', has_ring=True)
    )  # Saturn
    planets.append(
        Planet(3, 110, 18.0, symbol='♅', fill=';', color='bright_cyan')
    )  # Uranus
    planets.append(
        Planet(3, 130, 21.0, symbol='♆', fill='`', color='deep_sky_blue1')
    )  # Neptune
    planets.append(
        Planet(1, 150, 24.0, symbol='♇', color='bright_white')
    )  # Pluto


def add_random_solar_system(planets, min_planets=3, max_planets=10):
    """
    Populates the given list with a random number of randomised planets.

    Args:
        planets (list): The list to which Planet objects will be appended.
        min_planets (int): Minimum number of planets.
        max_planets (int): Maximum number of planets.

    Returns:
        None
    """
    sun_radius = random.randint(8, 14)
    sun_symbol = random.choice(BORDER_SYMBOLS)
    sun_fill = random.choice(FILL_SYMBOLS)
    sun_color = random.choice(PLANET_COLORS)

    sun = Sun(
            radius=sun_radius,
            symbol=sun_symbol,
            fill=sun_fill,
            color=sun_color
        )
    planets.append(sun)

    min_orbit_radius = ORBIT_RADIUS_MULTIPLIER * (sun_radius + sun.line_width)
    num_planets = random.randint(min_planets, max_planets)

    for _ in range(num_planets):
        radius = random.randint(MIN_RADIUS, MAX_RADIUS)
        orbit_radius = random.uniform(min_orbit_radius, MAX_ORBIT_RADIUS)
        period = random.uniform(MIN_PERIOD, MAX_PERIOD)
        symbol = random.choice(BORDER_SYMBOLS)
        fill = random.choice(FILL_SYMBOLS)
        color = random.choice(PLANET_COLORS)
        if random.random() < INCLINATION_CHANCE:
            inclination = random.uniform(0, MAX_INCLINATION)
        else:
            inclination = 0
        if random.random() < RING_CHANCE:
            has_ring = True
        else:
            has_ring = False

        planets.append(
            Planet(
                radius, orbit_radius, period,
                inclination=inclination,
                symbol=symbol,
                fill=fill,
                color=color,
                has_ring=has_ring
            )
        )
