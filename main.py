import argparse
from terminal_solar_system.main import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fps", type=int, default=30, help="Frames per second"
    )
    parser.add_argument(
        "--color", action="store_true", help="Enable color output"
    )
    args = parser.parse_args()
    main(fps=args.fps, color=args.color)
