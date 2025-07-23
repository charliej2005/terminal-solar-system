import math
import random

from terminal_solar_system.config import FPS
from terminal_solar_system.utils import polar_to_cartesian


class Planet:
    """Represents a planet."""

    def __init__(
        self,
        radius: float,
        orbit_radius: float,
        period: float,
        angle: float = None,
        inclination: float = 0.0,
        symbol: chr = "*",
        fill: chr = " ",
        line_width: float = 1,
        color: str = "white",
        x: float = 0,
        y: float = 0,
        z: float = 0,
    ):
        """Initialises new Planet.

        Args:
            radius (float): Width of the Planet.
            orbit_radius (float): Orbit radius of the Planet.
            period (float): Seconds needed for complete orbit.
            angle (float, optional): Angle of revolution in radians.
                Defaults to 0.0.
            inclination (float, optional): Angle of inclination in radians.
                Defaults to 0.0.
            symbol (chr, optional): Symbol used to draw the Planet border.
                Defaults to "*".
            fill (chr, optional): Symbol used to fill in planet border.
                Defaults to " ".
            line_width (float, optional): Width of drawn Planet border.
                Defaults to 1.
            color (str, optional): Color used to draw the Planet.
                Defaults to "white".
            x (float, optional): Initial x-coordinate of the Planet's center.
                Defaults to 0.
            y (float, optional): Initial y-coordinate of the Planet's center.
                Defaults to 0.
            z (float, optional): Initial z-coordinate of the Planet's center.
                Defaults to 0.
        """
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.period = period
        if angle is None:
            angle = random.uniform(0, 2 * math.pi)
        self.angle = angle
        self.inclination = inclination
        self.symbol = symbol
        self.fill = fill
        self.line_width = line_width
        self.color = color
        self.x = x
        self.y = y
        self.z = z

    def update(self):
        """Updates the planet when called to calculate new position.
        Should be called once per frame.

        Returns:
            None
        """
        if self.period == 0:
            return
        dt = 1 / FPS
        self.angle = (self.angle + (dt / self.period) * 2) % (2 * math.pi)
        self.x, self.y, self.z = polar_to_cartesian(
            self.orbit_radius, self.angle, self.inclination
        )
        return

    def __str__(self):
        """
        Returns a string representation of the planet's current state.

        Returns:
            str: String with planet parameters and position.
        """
        return (
            f"r: {self.radius}, r_o: {self.orbit_radius}, T: {self.period}, "
            f"θ: {self.angle}, φ: {self.inclination}, symbol: {self.symbol}, "
            f"fill: {self.fill}, line_width: {self.line_width}, "
            f"color: {self.color}, "
            f"x: {self.x}, y: {self.y}, z: {self.z}"
        )


class Sun(Planet):
    """Subclass of Planet representing a sun.
    This is what other planets orbit around."""

    def __init__(
        self,
        radius: float,
        symbol: chr = "*",
        fill: chr = " ",
        line_width: float = 3,
        color: str = "white",
    ):
        """Initialises new Sun.

        Args:
            radius (float): Width of the Sun.
            symbol (chr, optional): Symbol used to draw the Sun.
                Defaults to "*".
            fill (chr, optional): Symbol used to fill in planet border.
                Defaults to " ".
            line_width (float, optional): Width of drawn Sun border.
                Defaults to 3.
            color (str, optional): Color used to draw the Sun.
                Defaults to "white".
        """
        super().__init__(
            radius,
            0,
            0,
            0,
            0,
            symbol,
            fill,
            line_width,
            color,
        )
