from dataclasses import dataclass

@dataclass(frozen=True)
class Color():
    """An RGB color."""
    red: int
    green: int
    blue: int

    def __init__(self, red: int, green: int, blue: int):
        for key, value in {'red': red, 'green': green, 'blue': blue}.items():
            if value < 0:
                raise ValueError(f'{key} cannot be less than 0.')
            elif value > 255:
                raise ValueError(f'{key} cannot be greater than 255.')

        self.red = red
        self.green = green
        self.blue = blue
    
    def __iter__(self) -> tuple[int]:
        return (self.red, self.green, self.blue)


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GRAY = Color(127, 127, 127)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
CYAN = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)
