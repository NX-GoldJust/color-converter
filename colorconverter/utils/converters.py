import colorsys
from typing import Union
from dataclasses import dataclass
from enum import Enum, auto


class ColorType(Enum):
    HEX = auto()
    RGB = auto()
    HSV = auto()
    HSL = auto()
    CMYK = auto()
    YIQ = auto()
def hex_to_rgb(hex: str) -> tuple[float]:
    return tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

def hsv_to_rgb(hsv: tuple[float]) -> tuple[float]:
    return colorsys.hsv_to_rgb(*hsv)
def hsl_to_rgb(hsl: tuple[float]) -> tuple[float]:
    return colorsys.hls_to_rgb(*hsl)

def cmyk_to_rgb(cmyk: tuple[float]) -> tuple[float]:
    c, m, y, k = [color / 100.0 for color in cmyk]
    
    r = round(255 * (1 - c) * (1 - k))
    g = round(255 * (1 - m) * (1 - k))
    b = round(255 * (1 - y) * (1 - k))

    return float(r), (float(g)), float(b)


def yiq_to_rgb(yiq: tuple[float]) -> tuple[float]:
    return colorsys.yiq_to_rgb(*yiq)

@dataclass
class TempColor:
    hex: str
    rgb: tuple[float]
    hsv: tuple[float]
    hsl: tuple[float]
    cmyk: tuple[float]
    yiq: tuple[float]




class RGB:
    def __init__(self, rgb: tuple[Union[int, float]]) -> None:
        self.rgb = rgb
    
    def get_temp_color(self) -> TempColor:
        return TempColor(
            self.to_hex(),
            self.to_rgb(),
            self.to_hsv(),
            self.to_hsl(),
            self.to_cmyk(),
            self.to_yiq()
        )
        
    def to_hex(self) -> str:
        _rgb_int = [int(color) for color in self.rgb]
        return '#%02x%02x%02x' % tuple(_rgb_int)
    
    def to_rgb(self) -> tuple[float]:
        return (float(self.rgb[0]), float(self.rgb[1]), float(self.rgb[2]))

    def to_hsl(self) -> tuple[float]:
        # Conversion des valeurs de 0-255 à 0-1
        r, g, b = [color / 255.0 for color in self.rgb]

        # Conversion RGB vers HSL
        h, l, s = colorsys.rgb_to_hls(r, g, b)

        # Conversion des valeurs à l'échelle de 0-1 à 0-100
        h, l, s = round(h * 360), round(l * 100), round(s * 100)

        return (h, s, l)


    def to_hsv(self) -> tuple[float]:
            
        r, g, b = [color / 255.0 for color in self.rgb]

        # Conversion RGB vers HSV
        h, s, v = colorsys.rgb_to_hsv(r, g, b)

        # Conversion des valeurs à l'échelle de 0-1 à 0-100
        h, s, v = round(h * 360), round(s * 100), round(v * 100)

        return (h, s, v)
    
    def to_yiq(self) -> tuple[float]:
        return colorsys.rgb_to_yiq(*self.rgb)
        
    @property
    def saturation(self) -> float:
        return colorsys.rgb_to_hsv(*self.rgb)[1]
    def to_cmyk(self) -> tuple[float]:
        r, g , b = self.rgb
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        # Trouver la valeur maximale
        cmax = max(r, g, b)

        # Calcul du noir (K)
        k = 1 - cmax

        # Éviter une division par zéro si la couleur est noire
        if k == 1:
            c = m = y = 0
        else:
            # Calcul des composants CMY
            c = (1 - r - k) / (1 - k)
            m = (1 - g - k) / (1 - k)
            y = (1 - b - k) / (1 - k)

        # Conversion des valeurs à l'échelle de 0-1 à 0-100
        c, m, y, k = round(c * 100), round(m * 100), round(y * 100), round(k * 100)

        return (c, m, y, k)
    
    def __str__(self) -> str:
        return str(self.rgb)

def convert_to_rgb(value: str, type: ColorType) -> RGB:    
    _rgb = {
        ColorType.HEX: hex_to_rgb,
        ColorType.RGB: lambda x: x,
        ColorType.HSV: hsv_to_rgb,
        ColorType.HSL: hsl_to_rgb,
        ColorType.CMYK: cmyk_to_rgb,
        ColorType.YIQ: yiq_to_rgb
    }
    _color_rgb = _rgb.get(type, False)
    if _color_rgb == False:
        raise TypeError(f"Type {type} is not supported")
    return RGB(_color_rgb(value))