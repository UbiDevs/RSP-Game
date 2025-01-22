from config.createObjects import scr, btnRock, btnScissors, btnPaper, isChoice, player, computer


def choiceScreen():
    """
    This function handles the drawing and interaction of the choice screen in the game.
    It draws the buttons for rock, scissors, and paper, and displays the player and computer's choices.
    It also checks for button clicks and updates the player's choice accordingly.
    """
    # Draw the rock, scissors, and paper buttons
    btnRock.draw(scr.win)
    btnScissors.draw(scr.win)
    btnPaper.draw(scr.win)

    # Display the player's choice
    player.blitSign(sign = 'start', centerPos = (100, scr.size[1] // 2))

    # Display the computer's choice
    computer.blitSign(sign = 'start', centerPos = (scr.size[0] - 100, scr.size[1] // 2))

    # Check if any of the buttons have been clicked
    if btnRock.isClicked or btnScissors.isClicked or btnPaper.isClicked:
        # Change the isChoice variable to True
        isChoice.changeIsChoice

        # Set the player's choice based on which button was clicked
        if btnRock.isClicked:
            player.setChoice(value = 'rock')
        elif btnScissors.isClicked:
            player.setChoice(value = 'scissors')
        elif btnPaper.isClicked:
            player.setChoice(value = 'paper')

    # Reset the isClicked variables for the buttons
    btnRock.isClicked = btnScissors.isClicked = btnPaper.isClicked = False
    # Set the computer's choice
    computer.setChoice()