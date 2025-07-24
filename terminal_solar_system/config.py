import math

DEPTH_OF_FIELD_MODIFIER = 30
TERMINAL_X_SCALE = 2.2
STAR_FRAME_HOLD = 0.5

MIN_RADIUS = 1
MAX_RADIUS = 5
MAX_ORBIT_RADIUS = 120
MIN_PERIOD = 5
MAX_PERIOD = 30
INCLINATION_CHANCE = 0.2
MAX_INCLINATION = math.pi / 4
ORBIT_RADIUS_MULTIPLIER = 3

RING_CHAR = "/"
RING_SIZE_MODIFIER = 1.2
RING_CHANCE = 0.125

BORDER_SYMBOLS = [
    '*', 'O', '@', '#', '+', '-', '=', '~', '%', '$',
    '☀', '☿', '♀', '⊕', '♂', '♃', '♄', '♅', '♆', '♇'
]
FILL_SYMBOLS = [
    ' ', '.', ',', '`', '\'', ':', ';', '_', '^', '"', '/'
]
PLANET_COLORS = [
    'white', 'yellow', 'bright_yellow', 'gold',
    'red', 'bright_red', 'pink',
    'magenta', 'bright_magenta',
    'green', 'bright_green',
    'cyan', 'bright_cyan',
    'blue', 'bright_blue'
]
