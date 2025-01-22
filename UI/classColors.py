from dataclasses import dataclass, field

@dataclass(frozen = True)
class Colors:
    """
    The Colors class provides a set of predefined color constants, which can be used throughout the application.
    These colors can be represented as either a string name or a tuple of RGB values.

    Core Features:
    - Defines a set of color constants.
    - Supports both string and RGB tuple representations for colors.

    Example Usage:

    Constructor Parameters:
    - frozen (bool): A boolean flag indicating whether the class should be frozen. If True, the class cannot be modified after instantiation.

    Usage Limitations:
    - The class is designed to be immutable, meaning that once an instance is created, its attributes cannot be changed.
    - The class is not designed to be subclassed or extended.

    Potential Side Effects:
    - If the frozen parameter is set to False, the class can be modified after instantiation, which may lead to unexpected behavior in the application.
    """
    white: str | tuple[int, int, int] = field(default = 'white')
    yellow: str | tuple[int, int, int] = field(default = 'yellow')


