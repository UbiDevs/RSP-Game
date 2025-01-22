from dataclasses import dataclass, InitVar

@dataclass
class DrawText:
    """
    A class to render and display text on a screen.

    This class provides functionality to render text with a specified font, color, and position on a given screen.
    It uses the Pygame library to render the text and display it on the screen.

    Attributes:
        screen (object): The screen on which the text will be displayed.
        text (str): The text to be displayed.
        color (str | tuple[int, int, int]): The color of the text. Can be a string name or a tuple of RGB values.
        font (object): The font object used to render the text.
        pos (tuple): The position on the screen where the text will be displayed.

    Methods:
        __post_init__(self, text: str): Initializes the text attribute.
        update(self): Renders and displays the text on the screen.
    """

    screen: object = None
    text: InitVar[str] = ''
    color: str | tuple[int, int, int] = 'white'
    font: object = None
    pos: tuple = (0, 0)
    
    def __post_init__(self, text: str):
        """
        Initializes the text attribute.

        Args:
            text (str): The text to be displayed.
        """
        self.text = text if type(text) == str else str(text)
        
    
    def update(self):
        """
        Renders and displays the text on the screen.
        """
        self.textView = self.font.render(self.text, True, self.color)
        self.screen.blit(self.textView, self.pos)
