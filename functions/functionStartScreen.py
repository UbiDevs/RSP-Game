from config.createObjects import btnGroup, scr, isStart, player, computer

def startScreen():
    """
    This function handles the start screen of the game.
    It draws the start button and the signs for the player and computer.
    If the start button is clicked, it changes the game state to start.
    """
    # Draw the start button on the screen
    btnGroup[0].update(scr.win)
    # Draw the sign for the player on the screen
    player.update(sign = 'start')
    # Draw the sign for the computer on the screen
    computer.update(sign = 'start')

