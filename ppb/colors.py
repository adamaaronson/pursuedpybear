from dataclasses import dataclass
import colorsys

@dataclass()
class Color():
    """An RGB color, with red, green, and blue values ranging from 0-255."""
    red: int
    green: int
    blue: int

    def __post_init__(self):
        for key, value in {'red': self.red, 'green': self.green, 'blue': self.blue}.items():
            if value < 0:
                raise ValueError(f'{key} cannot be less than 0.')
            elif value > 255:
                raise ValueError(f'{key} cannot be greater than 255.')
    
    def __iter__(self):
        return (self.red, self.green, self.blue)

    @staticmethod
    def from_hsv(hue: float, saturation: float, value: float):
        """Convert the given HSV color values to an RGB color."""
        red, green, blue = colorsys.hsv_to_rgb(hue, saturation, value)
        return Color(int(red * 256), int(green * 256), int(blue * 256))


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GRAY = Color(127, 127, 127)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
CYAN = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)
