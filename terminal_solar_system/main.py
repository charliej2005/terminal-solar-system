from rich.console import Console
from rich.live import Live
from time import sleep
from renderer import render_frame
import shutil
from config import FPS
from planets import Planet, Sun


def main():
    """Runs a simple animated ASCII solar system in your Unix terminal."""
    width, height = shutil.get_terminal_size()
    console = Console()
    planets = []
    planets.append(Sun(10))
    planets.append(Planet(3, 40, 1, symbol='!'))
    planets.append(Planet(1, 50, 0.7, symbol='?'))
    planets.append(Planet(0.5, 70, 0.4, symbol='#'))
    with Live("", refresh_per_second=FPS, console=console) as live:
        while True:
            for planet in planets:
                planet.update()
            live.update(render_frame(planets, console.width, console.height))
            sleep(1 / FPS)


if __name__ == "__main__":
    main()
