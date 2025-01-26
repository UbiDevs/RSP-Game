from config.createObjects import player, computer, scores

def winScreen():
    """
    Displays the winning screen based on the scores of the player and the computer.

    This function checks the scores of the player and the computer and updates the
    signs displayed on their respective screens accordingly. If the player's score
    is higher than the computer's, the player's screen displays a 'win' sign and
    the computer's screen displays a 'start' sign. If the computer's score is higher
    than the player's, the computer's screen displays a 'win' sign and the player's
    screen displays a 'start' sign. If the scores are equal, both screens display
    a 'win' sign.
    """
    # Check if the player's score is higher than the computer's score
    if scores.playerScore > scores.computerScore:
        # Display a 'start' sign on the computer's screen and a 'win' sign on the player's screen
        computer.update(sign = 'start')
        player.update(sign = 'win')
    # Check if the computer's score is higher than the player's score
    elif scores.playerScore < scores.computerScore:
        # Display a 'win' sign on the computer's screen and a 'start' sign on the player's screen
        computer.update(sign = 'win')
        player.update(sign = 'start')
    else:
        computer.update(sign = 'win')
        player.update(sign = 'win')
        