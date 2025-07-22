from rich.console import Console
from rich.live import Live
from time import sleep
from renderer import render_frame
import shutil
from config import FPS


def main():
    """Runs a simple animated ASCII solar system in your Unix terminal."""
    width, height = shutil.get_terminal_size()
    console = Console()
    with Live("", refresh_per_second=FPS, console=console) as live:
        while True:
            live.update(render_frame(console.width, console.height))
            sleep(1 / FPS)


if __name__ == "__main__":
    main()
