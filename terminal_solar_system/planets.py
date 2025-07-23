from config import FPS
from utils import polar_to_cartesian
import math


class Planet:
    """Represents a planet."""

    def __init__(
        self,
        radius,
        orbit_radius,
        period,
        angle=0.0,
        symbol="*",
        line_width=1,
        color="white",
        x=0,
        y=0,
        z=0,
    ):
        """Initialises new Planet.

        Args:
            radius (int): Width in characters of the Planet.
            orbit_radius (int): Orbit radius in characters of the Planet.
            period (float): Seconds needed for complete orbit.
            angle (float): Angle of revolution in radians.
            symbol (str, optional): Symbol used to draw the Planet.
                Defaults to "*".
            line_width (int, optional): Width of drawn Planet border.
                Defaults to 1.
            color (str, optional): Color used to draw the Planet.
                Defaults to "white".
            x (float): x-coordinate of the Planet's center.
                Defaults to 0.
            y (float): y-coordinate of the Planet's center.
                Defaults to 0.
            z (float): z-coordinate of the Planet's center.
                Defaults to 0.
        """
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.period = period
        self.angle = angle
        self.symbol = symbol
        self.line_width = line_width
        self.color = color
        self.x = x
        self.y = y
        self.z = z

    def update(self):
        """Updates the planet when called to calculate new position.
        Should be called once per frame.
        """
        # TODO: implement functionality
        if self.period == 0:
            return
        dt = 1 / FPS
        self.angle = (self.angle + (dt / self.period) * 2) % (2 * math.pi)
        self.x, self.z = polar_to_cartesian(self.orbit_radius, self.angle)
        print(self)
        return

    def __str__(self):
        return (
            f"r: {self.radius}, r_o: {self.orbit_radius}, T: {self.period}, "
            f"θ: {self.angle}, symbol: {self.symbol}, "
            f"line_width: {self.line_width}, color: {self.color}, "
            f"x: {self.x}, y: {self.y}, z: {self.z}"
        )


class Sun(Planet):
    """Subclass of Planet representing a sun.
    This is what other planets orbit around."""

    def __init__(
        self,
        radius,
        symbol="*",
        line_width=3,
        color="white",
    ):
        """Initialises new Sun.

        Args:
            radius (int): Width in characters of the Sun.
            symbol (str, optional): Symbol used to draw the Sun.
                Defaults to "*".
            line_width (int, optional): Width of drawn Sun border.
                Defaults to 3.
            color (str, optional): Color used to draw the Sun.
                Defaults to "white".
        """
        super().__init__(
            radius,
            0,
            0,
            0,
            symbol,
            line_width,
            color,
        )
