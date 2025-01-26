from config.createObjects import scr, btnGroup, isChoice, player, computer


def choiceScreen():
    """
    This function handles the drawing and interaction of the choice screen in the game.
    It draws the buttons for rock, paper, and scissors, and displays the player and computer's choices.
    It also checks if a button has been clicked and updates the player's choice accordingly.
    """

    # Draw the rock, paper, and scissors buttons
    for btn in range(1, len(btnGroup)):
        btnGroup[btn].update(scr.win)

    # Display the player and computer's choices
    player.update(sign = 'start')
    computer.update(sign = 'start')

    if player.playerChoice:
        if not computer.playerChoice:
            computer.setChoice()
        isChoice.changeIsChoice