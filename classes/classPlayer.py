import pygame as pg
from pygame.transform import rotozoom, flip, scale
from pygame.image import load

from random import choice
from collections import OrderedDict
from dataclasses import dataclass, field

@dataclass
class Player:
    """
    The Player class represents a player in a game, managing their choices and visual representation on the screen.
    
    Attributes:
        name (str): The name of the player.
        autoGame (bool): Indicates if the game is in automatic mode.
        screen (object): The screen object where the player's choices are displayed.
        size (tuple): The size of the player's choices images.
        flStart (bool): Indicates if the game has started.
        flRotation (bool): Indicates if the player's choice is currently rotating.
        flWin (bool): Indicates if the player has won.
        centerPos (tuple): The center position of the player's choices on the screen.
        playerChoice (str): The player's current choice ('rock', 'paper', 'scissors', 'start', 'win').
        signDict (dict): A dictionary containing the images of the player's choices.
    
    Methods:
        __post_init__(): Initializes the player's choices images based on the game mode.
        setChoice(value='auto'): Sets the player's choice. If 'auto', the choice is randomly selected.
        rotation(angle=0): Rotates the player's choice image if the rotation flag is set.
        blitSign(sign=None, centerPos=None): Draws the player's choice image on the screen.
    """
    
    name: str = ''
    autoGame: bool = False
    screen: object = None
    size: tuple = (0, 0)
    flStart: bool = False
    flRotation: bool = False
    flWin: bool = False
    centerPos: tuple = (0, 0)

    playerChoice: str = ''
    signDict: dict = field(default_factory = OrderedDict)

    def __post_init__(self):
        # Load the rock image and scale it to the size of the game window
        self.signDict['rock'] = scale(load('images/rock.png'), self.size) if not self.autoGame else flip(scale(load('images/rock.png'), self.size), True, False)

        # Load the paper image and scale it to the size of the game window
        self.signDict['paper'] = scale(load('images/paper.png'), self.size) if not self.autoGame else flip(scale(load('images/paper.png'), self.size), True, False)

        # Load the scissors image and scale it to the size of the game window
        self.signDict['scissors'] = scale(load('images/scissors.png'), self.size) if not self.autoGame else flip(scale(load('images/scissors.png'), self.size), True, False)

        # Load the start image and scale it to the size of the game window
        self.signDict['start'] = scale(load('images/start.png'), self.size) if not self.autoGame else flip(scale(load('images/start.png'), self.size), True, False)
        # Get the rectangle of the start image and center it in the game window
        self.commonRect = self.signDict['start'].get_rect(center = self.centerPos)
        # Scale the start image to the size of the game window
        self.signRotation = scale(self.signDict['start'], self.signDict['start'].get_size())

        # Load the win image and scale it to the size of the game window
        self.signDict['win'] = flip(scale(load('images/win.png'), self.size), True, False) if not self.autoGame else scale(load('images/win.png'), self.size)

    def setChoice(self, value = 'auto'):
        # If the value is not 'auto', set the playerChoice to the value
        if value != 'auto':
            self.playerChoice = value
        # If the value is 'auto', set the playerChoice to a random choice from the first three keys of the signDict
        else:
            self.playerChoice = choice(list(self.signDict.keys())[: 3])

    def rotation(self, angle = 0):
        # If the rotation flag is true, set it to false and set the sign rotation to the start sign
        if self.flRotation:
            self.flRotation = False
            self.signRotation = self.signDict['start']
            # Get the rectangle of the sign rotation and set its center to the center position
            self.commonRect = self.signDict['start'].get_rect(center = self.centerPos)
        # If the rotation flag is false, set it to true and set the sign rotation to the start sign
        else:
            self.flRotation = True
            # Get the rectangle of the sign rotation and set its center to the center position minus 50 on the x-axis and plus 50 on the y-axis
            self.commonRect = self.signRotation.get_rect(center = (self.centerPos[0] - 50, self.centerPos[1] + 50))
            # Rotate the start sign by the given angle
            self.signRotation = rotozoom(self.signDict['start'], angle, 1)

    def update(self, sign = None):
        # If the object is not rotated, blit the sign to the screen at the commonRect position
        if not self.flRotation:
            self.screen.win.blit(self.signDict[sign], self.commonRect)
        # If the object is rotated, blit the rotated sign to the screen at the commonRect position
        else:
            self.screen.win.blit(self.signRotation, self.commonRect)
