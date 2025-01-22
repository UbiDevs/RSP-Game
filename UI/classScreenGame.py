from pygame.display import set_mode, set_caption, set_icon
from pygame.image import load
from dataclasses import dataclass


@dataclass
class ScreenGame:
    """
    ScreenGame is a class designed to initialize and manage a game window with customizable size, color, caption, and icon.
    
    Core functionalities include setting the window size, background color, window title, and window icon.
    
    Example usage:
    
    Parameters:
    - size (tuple): A tuple representing the width and height of the window.
    - color (str or tuple): The background color of the window. Can be a string name or a tuple of RGB values.
    - caption (str): The title of the window.
    - icon (str): The path to the icon file for the window.
    
    Note:
    - The `__post_init__` method is used to set up the window after initialization.
    - The `size` parameter is mandatory and must be a tuple.
    - The `color` parameter defaults to 'SteelBlue' if not provided.
    - The `caption` parameter defaults to 'Game' if not provided.
    - The `icon` parameter is optional and should be a valid file path to an image.
    """
    size: tuple = (800, 600)
    color: str | tuple[int, int, int] = 'SteelBlue'
    caption: str = 'Game'
    icon: str = ''

    def __post_init__(self):
        """
        This method is called after the initialization of the class. It sets up the window with the provided parameters.
        """
        # Set the window size
        self.win = set_mode(self.size)
        # Set the window caption
        self.caption = set_caption(self.caption)
        # If an icon is provided, set it
        if self.icon:
            self.icon = set_icon(load(self.icon))






