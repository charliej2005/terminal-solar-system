class Planet:
    """Represents a planet."""

    def __init__(
        self,
        radius,
        orbit_radius,
        period,
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
            period (int): Updates needed for complete orbit.
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
        return


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
            symbol,
            line_width,
            color,
        )
