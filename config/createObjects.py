"""
This Python script sets up a game of Rock-Paper-Scissors using a graphical user interface (GUI) and game logic.

The script imports various classes from different modules to manage the game's UI, logic, and player interactions. It initializes the game screen, players, scores, and buttons for the game. The game logic includes handling the start of the game, player choices, and rounds.

Classes and Modules:
- `UI.classColors`: Manages color settings for the game.
- `UI.classFonts`: Manages font settings for the game.
- `UI.classScreenGame`: Manages the game screen.
- `UI.classButton`: Manages button elements in the game.
- `logic.classRoundsCounter`: Manages the count of rounds in the game.
- `logic.classScores`: Manages the scores of the players.
- `logic.classIsStart`: Manages the start state of the game.
- `logic.classIsChoice`: Manages the player's choices.
- `logic.classRotationCounter`: Manages the rotation counter for the game.
- `classes.classPlayer`: Manages player data and interactions.
- `classes.classSoundGame`: Manages sound effects in the game.
"""


from UI.classColors import Colors
from UI.classFonts import Fonts
from UI.classScreenGame import ScreenGame
from UI.classButton import Button

from logic.classRoundsCounter import RoundsCounter
from logic.classScores import Scores
from logic.classIsStart import IsStart
from logic.classIsChoice import IsChoice
from logic.classRotationCounter import RotationCounter

from classes.classPlayer import Player
from classes.classSoundGame import SoundGame

scr = ScreenGame(size = (800, 600),
                 color = 'SteelBlue',
                 caption = 'Камень - Ножницы - Бумага',
                 icon = 'images/win.png')

isStart = IsStart()
isChoice = IsChoice()

scores = Scores()
roundsCounter = RoundsCounter(5)

colors = Colors()
fonts = Fonts()

rotationCounter = RotationCounter(6)
soundGame = SoundGame()

player = Player(name = 'Игрок',
                screen = scr,
                size = (144, 183),
                centerPos = (100, scr.size[1] // 2))

computer = Player(name = 'Компьютер',
                  autoGame = True,
                  screen = scr,
                  size = (144, 183),
                  centerPos = (scr.size[0] - 100, scr.size[1] // 2))

btnGroup = [Button(pos = (scr.size[0] // 2 - 100, scr.size[1] // 2),
                   size = (200, 50),
                   text = 'Старт',
                   onClickReferences = isStart.changeIsStart),
            Button(pos = (scr.size[0] // 2 - 175, scr.size[1] // 2 + 100),
                   size = (100, 50),
                   text = 'Камень',
                   referenceKwargs = dict(value = 'rock'),
                   onClickReferences = player.setChoice),
            Button(pos = (scr.size[0] // 2 - 50, scr.size[1] // 2 + 100),
                   size = (100, 50),
                   text = 'Ножницы',
                   referenceKwargs = dict(value = 'scissors'),
                   onClickReferences = player.setChoice),
            Button(pos = (scr.size[0] // 2 + 75, scr.size[1] // 2 + 100),
                   size = (100, 50),
                   text = 'Бумага',
                   referenceKwargs = dict(value = 'paper'),
                   onClickReferences = player.setChoice)]
