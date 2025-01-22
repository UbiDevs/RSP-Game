from config.createObjects import player, computer, scores

def roundScreen():
    """
    This function handles the logic for a single round of the game.
    It displays the player's and computer's choices, updates the scores based on the round result.
    """
    player.blitSign(sign = player.playerChoice)  # Display the player's choice

    computer.blitSign(sign = computer.playerChoice)  # Display the computer's choice

    # Determine the round result and update the scores accordingly
    if player.playerChoice == computer.playerChoice:
        scores.changeScores(0, 0)  # Draw
    elif player.playerChoice == 'rock' and computer.playerChoice == 'scissors':
        scores.changeScores(1, 0)  # Player wins
    elif player.playerChoice == 'scissors' and computer.playerChoice == 'paper':
        scores.changeScores(1, 0)  # Player wins
    elif player.playerChoice == 'paper' and computer.playerChoice == 'rock':
        scores.changeScores(1, 0)  # Player wins
    else:
        scores.changeScores(0, 1)  # Computer wins
