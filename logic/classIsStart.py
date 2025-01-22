from dataclasses import dataclass

@dataclass
class IsStart:
    """
    This class provides a simple mechanism to toggle a boolean state between True and False.
    
    Core Functionality:
    - The class has a single attribute `isStart` which is a boolean.
    - The `changeIsStart` property toggles the value of `isStart` between True and False.
    
    Usage:
    - To use this class, create an instance of `IsStart`.
    - Access the `isStart` attribute to get the current state.
    - Call the `changeIsStart` property to toggle the state.
    
    Example:
    
    Constructor Parameters:
    - None
    
    Special Usage Restrictions or Potential Side Effects:
    - None
    """
    
    isStart: bool = False
    
    @property
    def changeIsStart(self):
        self.isStart = not self.isStart
