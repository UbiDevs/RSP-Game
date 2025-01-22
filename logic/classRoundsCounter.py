from dataclasses import dataclass

@dataclass
class RoundsCounter:
    """
    RoundsCounter is a class designed to keep track of the number of rounds in a game or process.
    It provides a simple way to increase and decrease the count of rounds.

    Core Functionality:
    - Keeps track of the number of rounds.
    - Decreases the round count by one if it is greater than zero.

    Example Usage:

    Constructor:
    - No constructor parameters are required.

    Usage Limitations:
    - The decreaseRounds property will not decrease the round count below zero.
    """
    rounds: int = 0
    
    @property
    def decreaseRounds(self):
        if self.rounds > 0:
            self.rounds -= 1
