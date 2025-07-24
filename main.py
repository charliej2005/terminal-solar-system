"""Entry point for the Terminal Solar System simulation."""

import argparse
from terminal_solar_system.main import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--random", action="store_true", help="randomise planets"
    )
    parser.add_argument(
        "--color", action="store_true", help="enable color output"
    )
    parser.add_argument(
        "--fps", type=int, default=30, help="frames per second"
    )
    parser.add_argument(
        "--stars", type=int, default=100, help="stars in the background"
    )
    parser.add_argument(
        "--x-scale", type=float, default=2.2, help="font height/width ratio"
    )
    args = parser.parse_args()
    main(args.fps, args.color, args.stars, args.x_scale, args.random)
