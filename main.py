from rich import print
from rich.console import Console
from rich.live import Live
from time import sleep
from renderer import render_frame
import shutil


def main():
    """Runs a simple animated ASCII solar system in your Unix terminal."""
    width, height = shutil.get_terminal_size()
    console = Console()
    with Live("", refresh_per_second=10, console=console) as live:
        while True:
            live.update(render_frame(console.width, console.height))
            sleep(0.1)


if __name__ == "__main__":
    main()
