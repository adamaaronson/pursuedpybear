class Color():
    """An RGB color."""
    red: int
    green: int
    blue: int

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __repr__(self) -> str:
        return f'<{type(self).__name__} red={self.red} green={self.green} blue={self.blue}>'