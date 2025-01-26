import pygame as pg
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from config.createObjects import scr, btnGroup, isStart, isChoice, rotationCounter, roundsCounter, scores, soundGame, player, computer


from functions.functionStartScreen import startScreen
from functions.functionsChoiceScreen import choiceScreen
from functions.functionsRotationScreen import rotationScreen
from functions.functionCreateText import createText
from functions.functionRoundScreen import roundScreen
from functions.functionWinScreen import winScreen


class Game:
    """
    The Game class manages the main game loop and handles user interactions.
    
    Core functionalities:
    - Initializes game state and background music.
    - Processes events such as quitting the game or handling button presses.
    - Runs the game loop, updating the screen and handling game logic.
    
    Example usage:
    game = Game()
    game.runGame()
    
    Constructor parameters:
    - None
    
    Usage limitations:
    - The class assumes that the necessary Pygame modules and objects (e.g., pg, btnStart, btnRock, btnScissors, btnPaper, isStart, isChoice, rotationCounter, roundsCounter, scores, scr) are already initialized and available.
    - The class assumes that the necessary sound files and screen settings are correctly configured.
    """

    def __init__(self):
        # Initialize the game
        self.run = True
        # Create a clock object to control the frame rate
        self.clock = pg.time.Clock()
        # Play the background music
        soundGame.playBackgroundMusic('sounds/background_music.mp3')

    def eventGame(self):
        # Get all events from the event queue
        for event in pg.event.get():
            # If the event is a quit event or the escape key is pressed, set the run variable to False
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.run = False

            for btn in btnGroup:
                # If the button is clicked, call the handleEvent method of the button
                btn.handleEvent(event)

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
                        soundGame.playGameSound('sounds/counting_down.mp3')
                    # Call the rotationScreen method
                    rotationScreen()
                    # Decrease the rotationCounter variable
                    rotationCounter.decreaseCounter
                    # Update the display
                    pg.display.update()
                    # Delay for 500 milliseconds
                    pg.time.delay(500)
                # If the rotationCounter variable is 0, call the roundScreen method
                else:
                    # If the roundsCounter variable is greater than 0, decrease the roundsCounter variable
                    if roundsCounter.rounds > 0:
                        roundsCounter.decreaseRounds
                    # Reset the rotationCounter variable to 6
                    rotationCounter.counter = 6
                    isChoice.changeIsChoice
                    scr.win.fill(scr.color)
                    roundScreen()
                    createText()
                    pg.display.update()
                    pg.time.delay(2000)
                    player.playerChoice = False
                    computer.playerChoice = False

            if roundsCounter.rounds <= 0:
                scr.win.fill(scr.color)
                pg.mixer.music.pause()
                soundGame.playGameSound('sounds/victory.mp3')
                winScreen()
                createText()
                pg.display.update()
                pg.time.delay(3500)
                pg.mixer.music.unpause()
                roundsCounter.rounds = 5
                isStart.changeIsStart()
                scores.playerScore = 0
                scores.computerScore = 0


            pg.display.update()
