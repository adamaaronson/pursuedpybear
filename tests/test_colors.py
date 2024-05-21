import pytest
from ppb import Color, RGBColor, HSVColor
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
def test_rgb_color_validation(red, green, blue, should_raise):
    with pytest.raises(ValueError) if should_raise else does_not_raise():
        RGBColor(red, green, blue)

@pytest.mark.parametrize(
    ['hue', 'saturation', 'value', 'should_raise'],
    [
        [0, 0, 0, False],
        [360, 100, 100, False],
        [-1, 0, 0, True],
        [361, 0, 0, True],
        [0, -1, 0, True],
        [0, 101, 0, True],
        [0, 0, -1, True],
        [0, 0, 101, True],
    ]
)
def test_hsv_color_validation(hue, saturation, value, should_raise):
    with pytest.raises(ValueError) if should_raise else does_not_raise():
        HSVColor(hue, saturation, value)

@pytest.mark.parametrize(
    ['color', 'red', 'green', 'blue'],
    [
        [RGBColor(50, 40, 30), 50, 40, 30],
        [HSVColor(259, 46, 54.5), 95, 75, 139],
    ]
)
def test_to_rgb(color, red, green, blue):
    assert color.to_rgb() == (red, green, blue)