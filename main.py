import argparse
from terminal_solar_system.main import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--random", action="store_true", help="Randomise planets"
    )
    parser.add_argument(
        "--color", action="store_true", help="Enable color output"
    )
    parser.add_argument(
        "--fps", type=int, default=30, help="Frames per second"
    )
    parser.add_argument(
        "--stars", type=int, default=100, help="Stars in the background"
    )
    parser.add_argument(
        "--x-scale", type=float, default=2.2, help="Font height/width ratio."
    )
    args = parser.parse_args()
    main(args.fps, args.color, args.stars, args.x_scale, args.random)
