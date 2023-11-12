from dataclasses import dataclass
from typing import Union, Self
from ..utils.converters import convert_to_rgb, ColorType





class Color:
    value: str
    type: ColorType
    
    def __init__(self, value: Union[str, tuple[Union[int, float]]], type: ColorType) -> None:

        if type in [ColorType.HSV, ColorType.HSL, ColorType.CMYK, ColorType.YIQ, ColorType.HEX, ColorType.RGB]:
            self._value = convert_to_rgb(value, type).get_temp_color()
        else:
            raise TypeError(f"Type {type} is not supported")
    
    @property
    def rgb(self) -> tuple[float, float, float]:
        return self._value.rgb
    
    @property
    def hex(self) -> str:
        return self._value.hex
    
    @property
    def hsv(self) -> tuple[float, float, float]:
        return self._value.hsv
    
    @property
    def hsl(self) -> tuple[float, float, float]:
        return self._value.hsl
    
    @property
    def cmyk(self) -> tuple[float, float, float, float]:
        return self._value.cmyk
    
    @property
    def yiq(self) -> tuple[float, float, float]:
        return self._value.yiq
    
    def get_complementary(self) -> Self:
        r, g, b = self._value.rgb
        
        # Inversion of color
        r = 255 - r
        g = 255 - g
        b = 255 - b
        return Color((r, g, b), ColorType.RGB)
    
    def __str__(self) -> str:
        return self._value.hex

my_color = Color("#ff0000", ColorType.HEX)