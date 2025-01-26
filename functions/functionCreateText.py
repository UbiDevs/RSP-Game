from UI.classDrawText import DrawText
from UI.classTextGroup import TextGroup
from config.createObjects import scr, fonts, colors, roundsCounter, scores


def createText():
    """
    Creates a group of text elements to be displayed on the screen.

    The text group includes:
    - A text element showing the remaining rounds.
    - A text element showing the player's and computer's scores.

    The text elements are created with specific properties such as screen, font, color, position, and text content.
    """
    textGroup = TextGroup(group = [DrawText(screen = scr.win,
                                            font = fonts.roboto,
                                            color = colors.yellow,
                                            pos = (scr.size[0] // 2 - 190, 50),
                                            text = f'Осталось раундов: {roundsCounter.rounds}'),
                                   DrawText(screen = scr.win,
                                            font = fonts.roboto,
                                            color = colors.yellow,
                                            pos = (scr.size[0] // 2 - 30, scr.size[1] - 100),
                                            text = f'{scores.playerScore} : {scores.computerScore}'),])
    textGroup.update()
