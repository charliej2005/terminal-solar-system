from time import sleep

from rich.console import Console
from rich.live import Live

from terminal_solar_system.planets import Planet, Star, Sun
from terminal_solar_system.renderer import render_frame


def main(framerate, print_color, star_count):
    """Runs a simple animated ASCII solar system in your Unix terminal."""
    console = Console()
    stars = [Star(console) for _ in range(star_count)]
    planets = []
    add_solar_system(planets)
    with Live("", refresh_per_second=framerate, console=console) as live:
        while True:
            for star in stars:
                star.update()
            for planet in planets:
                planet.update(framerate)
            live.update(
                render_frame(
                    planets,
                    stars,
                    console,
                    print_color
                )
            )
            sleep(1 / framerate)


def add_solar_system(planets):
    """
    Populates the given list with Planet objects representing the solar system.

    Args:
        planets (list): The list to which Planet objects will be appended.

    Returns:
        None
    """
    planets.append(
        Sun(10, symbol='☀', fill='`', color='bright_yellow')
        )  # Sun
    planets.append(
        Planet(2, 25, 0.8, symbol='☿', color='bright_white')
    )  # Mercury
    planets.append(
        Planet(3, 35, 1.2, symbol='♀', fill=',', color='magenta1')
    )  # Venus
    planets.append(
        Planet(3, 45, 1.0, symbol='⊕', fill='`', color='deep_sky_blue1')
    )  # Earth
    planets.append(
        Planet(2, 55, 0.9, symbol='♂', fill='.', color='red1')
    )  # Mars
    planets.append(
        Planet(5, 70, 2.0, symbol='♃', fill='\'', color='gold1')
    )  # Jupiter
    planets.append(
        Planet(4, 90, 2.5, symbol='♄', fill=':', color='bright_cyan')
    )  # Saturn
    planets.append(
        Planet(3, 110, 3.0, symbol='♅', fill=';', color='cyan1')
    )  # Uranus
    planets.append(
        Planet(3, 130, 3.5, symbol='♆', fill='`', color='blue1')
    )  # Neptune
    planets.append(
        Planet(1, 150, 4.0, symbol='♇', color='white')
    )  # Pluto


if __name__ == "__main__":
    main()
