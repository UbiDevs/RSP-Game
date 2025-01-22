from pygame.transform import rotozoom, flip, scale
from pygame.image import load
from random import choice
from collections import OrderedDict

from dataclasses import dataclass, field


@dataclass
class Player:
    """
    The Player class represents a player in a game, managing their choices and visual representation.
    
    Attributes:
        name (str): The name of the player.
        autoGame (bool): Indicates if the game is in automatic mode.
        screen (object): The screen object where the player's visual representation is drawn.
        size (tuple): The size of the player's visual representation.
        flStart (bool): Indicates if the game has started.
        flRotation (bool): Indicates if the player's visual representation is rotating.
        flWin (bool): Indicates if the player has won.
        centerPos (tuple): The center position of the player's visual representation.
        playerChoice (str): The player's current choice.
        signDict (dict): A dictionary containing the player's visual representations for different choices.
    
    Methods:
        __post_init__(): Initializes the player's visual representations based on the game mode.
        setChoice(value='auto'): Sets the player's choice. If 'auto', the choice is randomly selected.
        rotation(angle=0): Rotates the player's visual representation if the rotation flag is set.
        blitSign(sign=None, centerPos=None): Draws the player's visual representation on the screen.
    """
    
    name: str = ''
    autoGame: bool = False
    screen: object = None
    size: tuple = (0, 0)
    flStart: bool = False
    flRotation: bool = False
    flWin: bool = False
    centerPos: tuple = (0, 0)
    
    playerChoice: str = None
    signDict: dict = field(default_factory = OrderedDict)
    
    def __post_init__(self):

        # Initialize the player's visual representations based on the game mode
        self.signDict['rock'] = scale(load('images/rock.png'), self.size) if not self.autoGame else flip(scale(load('images/rock.png'), self.size), True, False)

        self.signDict['scissors'] = scale(load('images/scissors.png'), self.size) if not self.autoGame else flip(scale(load('images/scissors.png'), self.size), True, False)

        self.signDict['paper'] = scale(load('images/paper.png'), self.size) if not self.autoGame else flip(scale(load('images/paper.png'), self.size), True, False)

        self.signDict['start'] = scale(load('images/start.png'), self.size) if not self.autoGame else flip(scale(load('images/start.png'), self.size), True, False)
        self.commonRect = self.signDict['start'].get_rect(center = self.centerPos)
        self.startRotation = scale(self.signDict['start'], self.signDict['start'].get_size())

        self.signDict['win'] = flip(scale(load('images/win.png'), self.size), True, False) if not self.autoGame else scale(load('images/win.png'), self.size)


    def setChoice(self, value = 'auto'):
        # Sets the player's choice. If 'auto', the choice is randomly selected.
        if value != 'auto':
            self.playerChoice = value
        else:
            self.playerChoice = choice(list(self.signDict.keys())[:3])

    def rotation(self, angle = 0):
        # Rotates the player's visual representation if the rotation flag is set.
        if self.flRotation:
            # If the rotation flag is set, set it to False and set the signRotation to the start sign.
            self.flRotation = False
            self.signRotation = self.signDict['start']
            # Set the commonRect to the start sign's rectangle, centered at the player's center position.
            self.commonRect = self.signDict['start'].get_rect(center = self.centerPos)
        else:
            # If the rotation flag is not set, set it to True and set the commonRect to the start sign's rectangle, centered at the player's center position minus 50 pixels in the x and y directions.
            self.flRotation = True
            self.commonRect = self.signDict['start'].get_rect(center = (self.centerPos[0] - 50, self.centerPos[1] + 50))
            # Set the signRotation to the start sign, rotated by the given angle.
            self.signRotation = rotozoom(self.signDict['start'], angle, 1)

    def blitSign(self, sign = None, centerPos = None):
        # Draws the player's visual representation on the screen.
        if not self.flRotation:
            # If the player is not rotating, draw the sign from the sign dictionary.
            self.screen.win.blit(self.signDict[sign], self.commonRect)
        else:
            # If the player is rotating, draw the rotated sign.
            self.screen.win.blit(self.signRotation, self.commonRect)



