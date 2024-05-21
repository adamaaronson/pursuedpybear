import pytest
from ppb import Color
from contextlib import nullcontext as does_not_raise

@pytest.mark.parametrize(
    ['red', 'green', 'blue', 'should_raise'],
    [
        [0, 0, 0, False],
        [255, 255, 255, False],
        [-1, 0, 0, True],
        [256, 0, 0, True],
        [0, -1, 0, True],
        [0, 256, 0, True],
        [0, 0, -1, True],
        [0, 0, 256, True],
    ]
)
def test_colors(red, green, blue, should_raise):
    with pytest.raises(ValueError) if should_raise else does_not_raise():
        Color(red, green, blue)

@pytest.mark.parametrize(
    ['hue', 'saturation', 'value', 'red', 'green', 'blue'],
    [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 255, 255, 255],
        [0, 1, 1, 255, 0, 0],
        [0.7189, 0.460, 0.545, 95, 75, 139],
    ]
)
def test_from_hsv(hue, saturation, value, red, green, blue):
    color = Color.from_hsv(hue, saturation, value)
    assert color == Color(red, green, blue)