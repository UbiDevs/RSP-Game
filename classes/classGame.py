import pygame as pg
from pygame.locals import *

from config.createObjects import scr, btnStart, btnRock, btnScissors, btnPaper, isStart, isChoice, rotationCounter, roundsCounter, soundGame, scores

from function.functionStartScreen import startScreen
from function.functionChoiceScreen import choiceScreen
from function.functionRotationScreen import rotationScreen
from function.functionRoundScreen import roundScreen
from function.functionCreateText import createText
from function.functionWinScreen import winScreen

class Game:
    """
    The Game class is responsible for managing the main game loop and handling user interactions.
    It initializes the game state, processes events, and updates the game screen accordingly.

    Core functionalities:
    - Initializes game state and background music.
    - Handles user events such as quitting the game or making choices.
    - Manages the game flow, including start screen, choice screen, rotation screen, and round screen.
    - Updates the game screen and handles game logic such as counting down, updating scores, and displaying victory screens.

    Usage:
    To use this class, create an instance of the Game class and call the runGame method to start the game loop.
    The class expects certain objects and variables to be defined in the global scope, such as:
    - pg: The Pygame module.
    - soundGame: An object with methods to play background music and game sounds.
    - btnStart, btnRock, btnScissors, btnPaper: Objects representing the start and choice buttons.
    - isStart, isChoice: Objects representing the game start and choice states.
    - rotationCounter, roundsCounter: Objects representing the rotation and rounds counters.
    - scr: An object representing the screen, with attributes win (the window surface) and color (the background color).
    - scores: An object representing the player and computer scores.

    Example:
    """

    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        soundGame.playBackgroundMusic(backMusic='sounds/background_music.mp3')

    def eventGame(self):
        # Get all events from the event queue
        for event in pg.event.get():
            # If the event is a quit event or the escape key is pressed, set the run variable to False
            if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.run = False

            # Handle events for the start button
            btnStart.handleEvent(event)
            # Handle events for the rock button
            btnRock.handleEvent(event)
            # Handle events for the scissors button
            btnScissors.handleEvent(event)
            # Handle events for the paper button
            btnPaper.handleEvent(event)

    def runGame(self):
        # Run the game while the run variable is True
        while self.run:
            # Fill the screen with the color specified in the screen class
            scr.win.fill(scr.color)

            # Call the eventGame method to handle events
            self.eventGame()

            # Call the createText method to create text on the screen
            createText()

            # If the isStart variable is False, call the startScreen method
            if not isStart.isStart:
                startScreen()
            # If the isStart variable is True and the isChoice variable is False, call the choiceScreen method
            elif isStart.isStart and not isChoice.isChoice:
                choiceScreen()
            # If the isStart variable is True and the isChoice variable is True, call the rotationScreen method
            elif isStart.isStart and isChoice.isChoice:
                # If the rotationCounter variable is greater than 0, call the rotationScreen method
                if rotationCounter.counter > 0:
                    # If the rotationCounter variable is even, play the counting_down sound
                    if rotationCounter.counter % 2 == 0:
                        soundGame.playGameSound(sound='sounds/counting_down.mp3')
                    # Call the rotationScreen method
                    rotationScreen()
                    rotationCounter.decreaseCounter
                    pg.display.update()
                    pg.time.delay(500)
                else:
                    if roundsCounter.rounds > 0:
                        roundsCounter.decreaseRounds
                    rotationCounter.counter = 6
                    isChoice.changeIsChoice
                    scr.win.fill(scr.color)
                    roundScreen()
                    createText()
                    pg.display.update()
                    pg.time.delay(2000)

            if roundsCounter.rounds <= 0:
                scr.win.fill(scr.color)
                soundGame.playGameSound(sound='sounds/victory.mp3')
                winScreen()
                createText()
                pg.display.update()
                pg.time.delay(2000)
                isStart.changeIsStart
                roundsCounter.rounds = 5
                scores.playerScore = 0
                scores.computerScore = 0

            pg.display.update()
