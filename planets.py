class Planet:
    """Represents a planet in Terminal Solar System."""

    def __init__(
        self,
        size,
        orbit_radius,
        period,
        symbol="#",
        color="white",
    ):
        """Initialises new Planet.

        Args:
            size (int): Width in characters of the planet
            orbit_radius (int): Orbit radius in characters of the planet
            period (int): Frames needed for complete orbit
            symbol (str, optional): Symbol used to draw the planet.
                Defaults to "#".
            color (str, optional): Color used to draw the planet.
                Defaults to "white".
        """
        self.size = size
        self.orbit_radius = orbit_radius
        self.period = period
        self.symbol = symbol
        self.color = color
