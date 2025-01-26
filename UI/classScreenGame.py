import pygame as pg
from pygame.display import set_mode, set_caption, set_icon
from pygame.image import load
from dataclasses import dataclass

@dataclass
class ScreenGame:
    """
    The ScreenGame class is designed to initialize and manage a game window with customizable size, color, and caption.

    Core functionalities:
    - Initializes a game window with specified size and color.
    - Sets the window caption.
    - Optionally sets the window icon.

    Parameters:
    - size (tuple): A tuple representing the width and height of the window.
    - color (str | tuple[int, int, int]): The background color of the window. Can be a string name or a tuple of RGB values.
    - caption (str): The title of the window.
    - icon (str): The path to the icon file for the window.

    Usage:
    """
    size: tuple = (0, 0)
    color: str | tuple[int, int, int] = 'SteelBlue'
    caption: str = 'Game'
    icon: str = ''

    def __post_init__(self):
        """
        Post-initialization method to set up the game window.
        """
        # Set the game window size
        self.win = set_mode(self.size)
        # Set the game window caption
        self.caption = set_caption(self.caption)
        # If an icon is provided, set it as the game window icon
        if self.icon:
            self.icon = set_icon(load(self.icon))

