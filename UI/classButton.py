import pygame as pg
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.font import Font, SysFont

from dataclasses import dataclass, InitVar


@dataclass
class Button:
    """
    A class representing a button with customizable properties such as position, size, text, image, and colors.

    Attributes:
        pos (tuple): Position of the button on the screen (x, y).
        size (tuple): Size of the button (width, height).
        text (str): Text displayed on the button.
        image (str): Image displayed on the button.
        font (InitVar[str]): Font used for the button text.
        fontSize (int): Font size for the button text.
        bgColor (str | tuple[int, int, int]): Background color of the button.
        textColor (str | tuple[int, int, int]): Text color of the button.
        hoverColor (str | tuple[int, int, int]): Color of the button when hovered.
        clickColor (str | tuple[int, int, int]): Color of the button when clicked.
        isHovered (bool): Whether the button is currently hovered.
        isClicked (bool): Whether the button is currently clicked.
        rect (pygame.Rect): Rectangle representing the button's area.

    Methods:
        __post_init__(font: str): Initializes the button's font.
        draw(surface): Draws the button on the given surface.
        handleEvent(event): Handles events such as mouse motion and button clicks.
    """

    pos: tuple = (0, 0)
    size: tuple = (10, 10)
    text: str = None
    image: str = None
    font: InitVar[str] = None
    fontSize = 26
    bgColor: str | tuple[int, int, int] = (144, 184, 218)
    textColor: str | tuple[int, int, int] = (255, 255, 255)
    hoverColor: str | tuple[int, int, int] = (23, 74, 117)
    clickColor: str | tuple[int, int, int] = (73, 107, 135)
    isHovered: bool = False
    isClicked: bool = False

    def __post_init__(self, font: str):
        """
        Initializes the button's font.
        Args:
            font (str): Font used for the button text.
        """
        # Create a rectangle for the button
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        # Set the font for the button text
        self.font = Font(font, self.fontSize) if font else SysFont('Arial', self.fontSize)

    def draw(self, surface):
        """
        Draws the button on the given surface.
        Args:
            surface (pygame.Surface): Surface to draw the button on.
        """
        # Check if the button is clicked
        if self.isClicked:
            # Set the color to the click color
            self.color = self.clickColor
        # Check if the button is hovered
        elif self.isHovered:
            # Set the color to the hover color
            self.color = self.hoverColor
        # If neither, set the color to the background color
        else:
            self.color = self.bgColor

        # Draw the button rectangle
        pg.draw.rect(surface, self.color, self.rect, border_radius = 20)
        
        # If there is text, draw it
        if self.text:
            # Render the text
            textSurface = self.font.render(self.text, True, self.textColor)
            # Get the rectangle of the text
            textRect = textSurface.get_rect(center = self.rect.center)
            # Draw the text on the surface
            surface.blit(textSurface, textRect)
            
        # If there is an image, draw it
        if self.image:
            # Get the rectangle of the image
            imageRect = self.image.get_rect(center = self.rect.center)
            # Draw the image on the surface
            surface.blit(self.image, imageRect)
    
    def handleEvent(self, event):
        """
        Handles events such as mouse motion and button clicks.
        Args:
            event (pygame.event.Event): Event to handle.
        """
        # Check if the event is a mouse motion event
        if event.type == MOUSEMOTION:
            # Check if the mouse is hovering over the button
            self.isHovered = self.rect.collidepoint(event.pos)
        # Check if the event is a mouse button down event
        elif event.type == MOUSEBUTTONDOWN:
            # Check if the left mouse button is pressed and the mouse is over the button
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.isClicked = True
        # Check if the event is a mouse button up event
            elif event.type == MOUSEBUTTONUP:
            # Set the isClicked attribute to False
                self.isClicked = False
