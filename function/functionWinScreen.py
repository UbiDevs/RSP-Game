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
    if scores.playerScore > scores.computerScore:
        computer.blitSign(sign = 'start')
        player.blitSign(sign = 'win')
    elif scores.playerScore < scores.computerScore:
        computer.blitSign(sign = 'win')
        player.blitSign(sign = 'start')
    else:
        computer.blitSign(sign = 'win')
        player.blitSign(sign = 'win')
