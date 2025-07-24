# Terminal Solar System

This Python project runs a simple ASCII solar system in your Unix terminal.

It's also my first [Boot.dev personal project](https://www.boot.dev/courses/build-personal-project-1), and showcases some of the Python skills I've picked up while following their Backend Developer course.
> Note: unlike the [guided projects](https://github.com/stars/charliej2005/lists/boot-dev), this project is entirely my own. 

---

### Features

- Animated ASCII planets and stars
- Vibrant color support made possible with [Rich](https://github.com/Textualize/rich)
- Dynamically adapts to terminal rescaling

---

### Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/charliej2005/terminal-solar-system.git
   cd terminal-solar-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python3 main.py
   ```

4. Optional flags:
   - `--color`: Enable vibrant color output
   - `--random`: Generate a random solar system
   - `--fps FPS`: Set frames per second (default: 30)
   - `--stars STARS`: Set number of background stars (default: 100)
   - `--x-scale X_SCALE`: Set terminal font aspect ratio (default: 2.2)

---

Have fun! :)

> This tool is not accurate to real-world orbits.
> If you're an astronomer, please avert your eyes!