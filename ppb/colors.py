from dataclasses import dataclass
from abc import ABC, abstractmethod
import colorsys

class Color(ABC):
    """Abstract base class for a color."""
    @abstractmethod
    def to_rgb(self):
        """Convert to a tuple of red, green, and blue values."""
        pass


@dataclass(frozen=True)
class RGBColor(Color):
    """An RGB color, with red, green, and blue values ranging from 0 to 255."""
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

    def to_rgb(self):
        return (self.red, self.green, self.blue)


@dataclass(frozen=True)
class HSVColor(Color):
    """
    An HSV color, with hue ranging from 0 to 360,
    saturation ranging from 0 to 100, and value ranging from 0 to 100.
    """
    hue: float
    saturation: float
    value: float

    def __post_init__(self):
        for key, (value, max_value) in {
            'hue': (self.hue, 360),
            'saturation': (self.saturation, 100),
            'value': (self.value, 100),
        }.items():
            if value < 0:
                raise ValueError(f'{key} cannot be less than 0.')
            elif value > max_value:
                raise ValueError(f'{key} cannot be greater than {max_value}.')

    def to_rgb(self):
        red, green, blue = colorsys.hsv_to_rgb(self.hue / 360, self.saturation / 100, self.value / 100)
        return (round(red * 255), round(green * 255), round(blue * 255))


BLACK = RGBColor(0, 0, 0)
WHITE = RGBColor(255, 255, 255)
GRAY = RGBColor(127, 127, 127)
RED = RGBColor(255, 0, 0)
GREEN = RGBColor(0, 255, 0)
BLUE = RGBColor(0, 0, 255)
CYAN = RGBColor(0, 255, 255)
MAGENTA = RGBColor(255, 0, 255)
YELLOW = RGBColor(255, 255, 0)
