from config.createObjects import player, computer, scores

def roundScreen():
    """
    This function handles the logic for a single round of the game.
    It displays the player's and computer's choices, and updates the scores based on the game rules.
    """
    # Display the player's choice
    player.update(sign = player.playerChoice)
    # Display the computer's choice
    computer.update(sign = computer.playerChoice)

    # If the player's choice is the same as the computer's choice, change the scores
    if player.playerChoice == computer.playerChoice:
        scores.changeScores()
    # If the player's choice is rock and the computer's choice is scissors, change the scores
    elif player.playerChoice == 'rock' and computer.playerChoice == 'scissors':
        scores.changeScores(1, 0)
    # If the player's choice is paper and the computer's choice is rock, change the scores
    elif player.playerChoice == 'paper' and computer.playerChoice == 'rock':
        scores.changeScores(1, 0)
    # If the player's choice is scissors and the computer's choice is paper, change the scores
    elif player.playerChoice == 'scissors' and computer.playerChoice == 'paper':
        scores.changeScores(1, 0)
    # Otherwise, change the scores
    else:
        scores.changeScores(0, 1)
