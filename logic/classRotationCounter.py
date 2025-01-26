
from dataclasses import dataclass


@dataclass
class RotationCounter:
    """
    RotationCounter is a class designed to keep track of a counter value that can be increased or decreased.
    
    Core Functionality:
    - Keeps track of a counter value.
    - Decreases the counter value by 1 if it is greater than 0.
    
    Example Usage:
    
    Constructor:
    - No constructor parameters are required.
    
    Limitations and Side Effects:
    - The counter value cannot be set to a negative number.
    """
    counter: int = 0
    
    @property
    def decreaseCounter(self):
        if self.counter > 0:
            self.counter -= 1
