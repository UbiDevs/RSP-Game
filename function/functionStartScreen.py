from config.createObjects import btnStart, scr, isStart, player, computer

def startScreen():
    """
    This function handles the drawing and interaction of the start screen.

    It draws the start button and the signs for the player and computer.
    If the start button is clicked, it changes the state of the game to start.
    """
    btnStart.draw(scr.win)

    player.blitSign(sign = 'start')

    computer.blitSign(sign = 'start')

    if btnStart.isClicked:
        btnStart.isClicked = False
        isStart.changeIsStart
