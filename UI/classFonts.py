from pygame.font import SysFont
from dataclasses import dataclass


@dataclass(frozen = True)
class Fonts:
    """
    The Fonts class provides access to predefined font objects for use in a graphical application.
    
    Core functionality:
    - Provides access to two predefined fonts: Arial and Roboto.
    
    Usage:
    - This class is designed to be used as a static class, with the fonts being accessed directly through the class attributes.
    
    Example:
    
    Constructor parameters:
    - None
    
    Special usage considerations:
    - This class is immutable, as indicated by the 'froze' attribute set to True.
    - The fonts are initialized with specific sizes (36 for Arial and 55 for Roboto), which cannot be changed.
    """
    arial: object = SysFont('Arial', 36)
    roboto: object = SysFont('Roboto', 55)


