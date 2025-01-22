from dataclasses import dataclass

@dataclass
class RotationCounter:
    """
    The RotationCounter class is designed to manage a counter that starts at a specified value and can be decreased by a method.
    
    Core Functionality:
    - Decrease the counter by 1 if it is greater than 0.
    
    Example Usage:
    
    Constructor:
    - No constructor parameters are required.
    
    Limitations and Side Effects:
    - The counter cannot be increased directly. It can only be decreased.
    - The counter will never go below 0.
    """
    
    counter: int = 6
    
    @property
    def decreaseCounter(self):
        if self.counter > 0:
            self.counter -= 1
