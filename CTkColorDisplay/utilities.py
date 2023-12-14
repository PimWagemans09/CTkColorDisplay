import re
from .exceptions import invalidHexException

def verify_hex(hex:str) -> bool:
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex)
    if match:
        return True
    return False

def hex_to_rgb(color:str) -> tuple:
    if not verify_hex(color):
        raise invalidHexException(f"\"{color}\" is not a valid hex color")
    hex = color.lstrip('#')
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def rgb_to_hex(color: tuple) -> str:
    return '#%02X%02X%02X' % color