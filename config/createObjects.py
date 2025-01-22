'''
This Python code snippet is designed to create a graphical user interface (GUI) for a Rock-Paper-Scissors game. The code imports various classes and modules that are likely part of a larger project, and it initializes several objects that will be used to create and manage the game's interface and logic. Here's a breakdown of the code:

### Imports
The code imports several classes and modules from different namespaces, which are likely part of a larger library or framework designed for creating GUI applications. These imports include:

- `ScreenGame`, `Button`, `Colors`, `DrawText`, `Fonts` from `UI` namespace: These classes are used to create the game's screen, buttons, colors, text drawing, and fonts.
- `IsStart`, `IsChoice`, `Scores`, `RoundsCounter`, `RotationCounter` from `logic` namespace: These classes handle the game's logic, such as determining if the game has started, making choices, keeping scores, counting rounds, and rotating choices.
- `Player`, `SoundGame` from `classes` namespace: These classes manage the player's actions and the game's sound effects.

### Screen Initialization
A `ScreenGame` object named `scr` is created with the following parameters:
- `size`: The dimensions of the game window (800x600 pixels).
- `color`: The background color of the window ('SteelBlue').
- `caption`: The title of the window ('Камень Ножницы Бумага', which translates to 'Rock-Paper-Scissors').
- `icon`: The icon for the window ('images/win.png').

### Game Logic Initialization
Several objects are initialized to manage the game's logic:
- `isStart`: Manages the start state of the game.
- `isChoice`: Manages the player's and computer's choices.
- `scores`: Manages the scores of the game.
- `roundsCounter`: Counts the number of rounds (5 rounds in this case).
- `colors`: Manages the colors used in the game.
- `fonts`: Manages the fonts used in the game.
- `rotationCounter`: Manages the rotation of choices.

### Player Initialization
Two `Player` objects are created:
- `player`: Represents the human player with the name 'Игрок' (Player) and is positioned at the left side of the screen.
- `computer`: Represents the computer player with the name 'Компьютер' (Computer) and is positioned at the right side of the screen. The `autoGame` parameter is set to `True`, indicating that the computer will make automatic choices.

### Button Initialization
Four `Button` objects are created to represent the choices in the game:
- `btnStart`: A button to start the game, positioned in the center of the screen.
- `btnRock`: A button for the 'Rock' choice, positioned slightly to the left of the center.
- `btnScissors`: A button for the 'Scissors' choice, positioned in the center.
- `btnPaper`: A button for the 'Paper' choice, positioned slightly to the right of the center.

### Sound Initialization
A `SoundGame` object named `soundGame` is created to manage the game's sound effects.

### Summary
This code sets up the basic structure for a Rock-Paper-Scissors game with a graphical user interface. It initializes the game window, players, buttons for choices, and various game logic components. The actual game logic, event handling, and rendering would be implemented in additional parts of the code that are not shown here.

'''

from UI.classScreenGame import ScreenGame
from UI.classButton import Button
from UI.classColors import Colors
from UI.classDrawText import DrawText
from UI.classFonts import Fonts

from logic.classIsStart import IsStart
from logic.classIsChoice import IsChoice
from logic.classScores import Scores
from logic.classRoundsCounter import RoundsCounter
from logic.classRotationCounter import RotationCounter

from classes.classPlayer import Player
from classes.classSoundGame import SoundGame

scr = ScreenGame(size = (800, 600), 
                      color = 'SteelBlue',
                      caption = 'Камень Ножницы Бумага',
                      icon = 'images/win.png')

isStart = IsStart()
isChoice = IsChoice()
scores = Scores()
roundsCounter = RoundsCounter(5)
colors = Colors()
fonts = Fonts()
rotationCounter = RotationCounter()

player = Player(name = 'Игрок',
                screen = scr,
                size = (144, 183),
                centerPos = (100, scr.size[1] / 2))

computer = Player(name = 'Компьютер',
                autoGame = True,
                screen = scr,
                size = (144, 183),
                centerPos = (scr.size[0] - 100, scr.size[1] / 2))

btnStart = Button(pos = (scr.size[0] / 2 - 100, scr.size[1] / 2),
                    size = (200, 50),
                    text = 'Старт')

btnRock = Button(pos = (scr.size[0] / 2 - 175, scr.size[1] / 2 + 100),
                    size = (100, 50),
                    text = 'Камень')

btnScissors = Button(pos = (scr.size[0] / 2 - 50, scr.size[1] / 2 + 100),
                    size = (100, 50),
                    text = 'Ножницы')

btnPaper = Button(pos = (scr.size[0] / 2 + 75, scr.size[1] / 2 + 100),
                    size = (100, 50),
                    text = 'Бумага')

soundGame = SoundGame()