import unittest
from planets import Planet


class TestPlanet(unittest.TestCase):
    def test_planet_update(self):
        planet = Planet(3, 5, 5)
        print(planet.update())


if __name__ == '__main__':
    unittest.main()
