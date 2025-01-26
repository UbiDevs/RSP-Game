from dataclasses import dataclass

@dataclass
class Scores:
    """
    A class to keep track of scores for a game between a player and a computer.

    Attributes:
        playerScore (int): The score of the player.
        computerScore (int): The score of the computer.

    Methods:
        changeScores(playerScore=0, computerScore=0): Updates the scores of the player and the computer.
    """

    playerScore: int = 0
    computerScore: int = 0
    
    def changeScores(self, playerScore = 0, computerScore = 0):
        """
        Updates the scores of the player and the computer.

        Args:
            playerScore (int): The score to add to the player's score. Defaults to 0.
            computerScore (int): The score to add to the computer's score. Defaults to 0.
        """
        self.playerScore += playerScore
        self.computerScore += computerScore
