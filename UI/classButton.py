import pygame as pg
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.font import Font, SysFont

from dataclasses import dataclass, field, InitVar


@dataclass
class Button:
    """
    A class representing a button with customizable properties and behaviors.

    This class provides a way to create a button with various visual and functional properties.
    It supports text and image rendering, color changes on hover and click, and event handling.
    The button can also execute a reference function when clicked.

    Attributes:
        pos (tuple): Position of the button on the screen (x, y).
        size (tuple): Size of the button (width, height).
        text (str): Text to be displayed on the button.
        image (str): Path to the image to be displayed on the button.
        font (InitVar[str]): Font to be used for the button text.
        font_size (int): Size of the font.
        bgColor (str | tuple[int, int, int]): Background color of the button.
        textColor (str | tuple[int, int, int]): Text color of the button.
        hoverColor (str | tuple[int, int, int]): Color of the button when hovered.
        clickColor (str | tuple[int, int, int]): Color of the button when clicked.
        isHovered (bool): Whether the button is currently hovered.
        isClicked (bool): Whether the button is currently clicked.
        onClickReferences (object): Reference to a function to be called when the button is clicked.
        referenceArgs (tuple): Arguments to be passed to the onClickReferences function.
        referenceKwargs (dict): Keyword arguments to be passed to the onClickReferences function.

    Methods:
        __post_init__(font: str): Initializes the button's font.
        update(surface): Updates the button's appearance on the given surface.
        handleEvent(event): Handles events related to the button.
        clickEvent(): Executes the onClickReferences function with the provided arguments.
    """

    pos: tuple = (0, 0)
    size: tuple = (0, 0)
    text: str = None
    image: str = None
    font: InitVar[str] = None
    font_size: int = 26
    bgColor: str | tuple[int, int, int] = (144, 184, 218)
    textColor: str | tuple[int, int, int] = (255, 255, 255)
    hoverColor: str | tuple[int, int, int] = (23, 74, 117)
    clickColor: str | tuple[int, int, int] = (73, 107, 135)
    isHovered: bool = False
    isClicked: bool = False
    onClickReferences: object = None
    referenceArgs: tuple = field(default_factory = tuple)
    referenceKwargs: dict = field(default_factory = dict)

    def __post_init__(self, font: str):
        """
        Initialize the rectangle and font attributes for the Text object.

        Args:
            font (str): The name of the font to use. If None, use the system default font 'Arial'.
        """
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.font = Font(font, self.font_size) if font else SysFont('Arial', self.font_size)

    def update(self, surface):
        """
        Updates the appearance of the button on the given surface.

        Args:
            surface (pygame.Surface): The surface on which the button is drawn.
        """
        if self.isClicked:
            self.color = self.clickColor
        elif self.isHovered:
            self.color = self.hoverColor
        else:
            self.color = self.bgColor

        pg.draw.rect(surface, self.color, self.rect, border_radius = 20)

        if self.text:
            testSurface = self.font.render(self.text, True, self.textColor)
            textRect = testSurface.get_rect(center=self.rect.center)
            surface.blit(testSurface, textRect)

    def handleEvent(self, event):
        """
        Handle different types of mouse events.

        Args:
            event (pygame.event.Event): The event to handle.

        Returns:
            None
        """
        if event.type == MOUSEMOTION:
            """
            Check if the mouse is hovering over the rectangle.
            """
            self.isHovered = self.rect.collidepoint(event.pos)
        elif event.type == MOUSEBUTTONDOWN:
            """
            Check if the left mouse button is pressed and if the mouse is within the rectangle.
            """
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.isClicked = True
                if self.onClickReferences:
                    self.clickEvent()
        elif event.type == MOUSEBUTTONUP:
            """
            Set the isClicked flag to False when the left mouse button is released.
            """
            self.isClicked = False

    def clickEvent(self):
        """
        Handle the click event based on the presence of positional and keyword arguments.

        This method checks if there are positional arguments (`referenceArgs`) and/or keyword arguments
        (`referenceKwargs`) and calls the `onClickReferences` method accordingly. If both are present, it
        calls `onClickReferences` with both types of arguments. If only positional arguments are present,
        it calls `onClickReferences` with positional arguments. If only keyword arguments are present,
        it calls `onClickReferences` with keyword arguments. If neither are present, it calls
        `onClickReferences` without any arguments.
        """
        if self.referenceArgs and not self.referenceKwargs:
            self.onClickReferences(*self.referenceArgs)
        elif self.referenceKwargs and not self.referenceArgs:
            self.onClickReferences(**self.referenceKwargs)
        elif self.referenceArgs and self.referenceKwargs:
            self.onClickReferences(*self.referenceArgs, **self.referenceKwargs)
        else:
            self.onClickReferences()
