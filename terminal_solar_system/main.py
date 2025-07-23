import math
import shutil
from time import sleep

from rich.console import Console
from rich.live import Live

from terminal_solar_system.config import FPS
from terminal_solar_system.planets import Planet, Sun
from terminal_solar_system.renderer import render_frame


def main():
    """Runs a simple animated ASCII solar system in your Unix terminal."""
    width, height = shutil.get_terminal_size()
    console = Console()
    planets = []
    add_solar_system(planets)
    with Live("", refresh_per_second=FPS, console=console) as live:
        while True:
            for planet in planets:
                planet.update()
            live.update(render_frame(planets, console.width, console.height))
            sleep(1 / FPS)


def add_solar_system(planets):
    planets.append(Sun(10, symbol='☀', color='bright_yellow'))  # Sun
    planets.append(
        Planet(2, 25, 0.8, symbol='☿', color='bright_white')
    )  # Mercury
    planets.append(Planet(3, 35, 1.2, symbol='♀', color='magenta1'))  # Venus
    planets.append(
        Planet(3, 45, 1.0, symbol='⊕', color='deep_sky_blue1')
    )  # Earth
    planets.append(
        Planet(2, 55, 0.9, symbol='♂', color='red1')
    )  # Mars
    planets.append(
        Planet(5, 70, 2.0, symbol='♃', color='gold1')
    )  # Jupiter
    planets.append(
        Planet(4, 90, 2.5, symbol='♄', color='bright_cyan')
    )  # Saturn
    planets.append(
        Planet(3, 110, 3.0, symbol='♅', color='cyan1')
    )  # Uranus
    planets.append(
        Planet(3, 130, 3.5, symbol='♆', color='blue1')
    )  # Neptune
    planets.append(
        Planet(1, 150, 4.0, symbol='♇', color='white')
    )  # Pluto

if __name__ == "__main__":
    main()
