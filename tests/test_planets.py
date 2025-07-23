import math
import unittest

from terminal_solar_system.planets import Planet, Sun


class TestPlanet(unittest.TestCase):
    def test_planet_initialization_defaults(self):
        planet = Planet(
            10, 4, 8
        )
        self.assertEqual(planet.radius, 10)
        self.assertEqual(planet.orbit_radius, 4)
        self.assertEqual(planet.period, 8)
        self.assertEqual(planet.angle, 0.0)
        self.assertEqual(planet.symbol, "*")
        self.assertEqual(planet.line_width, 1)
        self.assertEqual(planet.color, "white")
        self.assertEqual(planet.x, 0)
        self.assertEqual(planet.y, 0)
        self.assertEqual(planet.z, 0)

    def test_planet_initialization_custom(self):
        planet = Planet(
            2, 10, 20,
            angle=math.pi/4,
            symbol='@',
            line_width=2,
            color='blue',
            x=1, y=2, z=3
        )
        self.assertEqual(planet.radius, 2)
        self.assertEqual(planet.orbit_radius, 10)
        self.assertEqual(planet.period, 20)
        self.assertAlmostEqual(planet.angle, math.pi/4)
        self.assertEqual(planet.symbol, '@')
        self.assertEqual(planet.line_width, 2)
        self.assertEqual(planet.color, 'blue')
        self.assertEqual(planet.x, 1)
        self.assertEqual(planet.y, 2)
        self.assertEqual(planet.z, 3)

    def test_planet_initialization_custom_shuffled(self):
        planet = Planet(
            2, 10, 20,
            color='green',
            z=9,
            angle=math.pi/2,
            symbol='#',
            y=8,
            x=7,
            line_width=3
        )
        self.assertEqual(planet.radius, 2)
        self.assertEqual(planet.orbit_radius, 10)
        self.assertEqual(planet.period, 20)
        self.assertAlmostEqual(planet.angle, math.pi/2)
        self.assertEqual(planet.symbol, '#')
        self.assertEqual(planet.line_width, 3)
        self.assertEqual(planet.color, 'green')
        self.assertEqual(planet.x, 7)
        self.assertEqual(planet.y, 8)
        self.assertEqual(planet.z, 9)

    def test_planet_update_basic(self):
        planet = Planet(3, 5, 5)
        old_angle = planet.angle
        old_x = planet.x
        old_z = planet.z
        planet.update()
        self.assertNotEqual(planet.angle, old_angle)
        self.assertNotEqual((planet.x, planet.z), (old_x, old_z))

    def test_planet_update_no_period(self):
        planet = Planet(3, 5, 0)
        old_angle = planet.angle
        old_x = planet.x
        old_z = planet.z
        planet.update()
        self.assertEqual(planet.angle, old_angle)
        self.assertEqual(planet.x, old_x)
        self.assertEqual(planet.z, old_z)

    def test_planet_update_angle_wraps(self):
        planet = Planet(1, 10, 1, angle=2 * math.pi - 0.01)
        planet.update()
        self.assertTrue(0 <= planet.angle < 2 * math.pi)

    def test_planet_str(self):
        planet = Planet(1, 2, 3, angle=0.5, symbol='!', line_width=1, color='red', x=4, y=5, z=6)
        s = str(planet)
        self.assertIn("r: 1", s)
        self.assertIn("r_o: 2", s)
        self.assertIn("T: 3", s)
        self.assertIn("θ: 0.5", s)
        self.assertIn("symbol: !", s)
        self.assertIn("color: red", s)
        self.assertIn("x: 4", s)
        self.assertIn("y: 5", s)
        self.assertIn("z: 6", s)


class TestSun(unittest.TestCase):
    def test_sun_initialization(self):
        sun = Sun(10, symbol='O', line_width=5, color='yellow')
        self.assertEqual(sun.radius, 10)
        self.assertEqual(sun.orbit_radius, 0)
        self.assertEqual(sun.period, 0)
        self.assertEqual(sun.angle, 0)
        self.assertEqual(sun.symbol, 'O')
        self.assertEqual(sun.line_width, 5)
        self.assertEqual(sun.color, 'yellow')

    def test_sun_update(self):
        sun = Sun(10)
        old_angle = sun.angle
        old_x = sun.x
        old_z = sun.z
        sun.update()
        self.assertEqual(sun.angle, old_angle)
        self.assertEqual(sun.x, old_x)
        self.assertEqual(sun.z, old_z)


if __name__ == '__main__':
    unittest.main()
