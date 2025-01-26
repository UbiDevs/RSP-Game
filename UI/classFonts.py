import pygame as pg
from pygame.font import SysFont
from dataclasses import dataclass

@dataclass(frozen = True)
class Fonts:
    """
    Fonts class provides access to system fonts 'Arial' and 'Roboto' with specified sizes.

    Core functionality:
    - Provides access to two system fonts: 'Arial' and 'Roboto'.
    - Initializes the fonts with specified sizes.

    Usage:
    - To use the fonts, simply access the class attributes 'arial' and 'roboto'.
    - Example:
        >>> from pygame import font
        >>> from fonts import Fonts
        >>> fonts = Fonts()
        >>> arial_font = fonts.arial
        >>> roboto_font = fonts.roboto
    """

    arial: object = SysFont('Arial', 36)
    roboto: object = SysFont('Roboto', 55)
