from UI.classDrawText import DrawText
from classes.classTextGroup import TextGroup
from config.createObjects import scr, fonts, colors, roundsCounter, scores


def createText():
    """
    Creates a TextGroup object containing two DrawText objects.
    The first DrawText object displays the remaining rounds.
    The second DrawText object displays the player and computer scores.
    """
    textGroup = TextGroup(group = [DrawText(screen = scr.win,
                                            font = fonts.roboto,
                                            color = colors.yellow,
                                            pos = (scr.size[0] / 2 - 190, 50),
                                            text = f'Осталось раундов: {roundsCounter.rounds}'),
                                   DrawText(screen = scr.win,
                                            font = fonts.roboto,
                                            color = colors.yellow,
                                            pos = (scr.size[0] // 2 - 30, scr.size[1] - 100),
                                            text = f'{scores.playerScore} - {scores.computerScore}'),
                                        ])
    textGroup.update()
