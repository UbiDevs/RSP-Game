from dataclasses import dataclass

@dataclass(frozen = True)
class Colors:
    """
    The Colors class provides predefined color constants in both string and RGB tuple formats.

    Core Functionality:
    - Defines color constants in both string and RGB tuple formats.

    Usage:
    - This class is intended to be used as a reference for color constants in your application.
    - It can be imported and used directly to access predefined colors.

    Example:

    Constructor Parameters:
    - None

    Special Usage Restrictions:
    - This class does not have any constructor parameters.
    - It is a static class that provides read-only access to predefined color constants.

    Potential Side Effects:
    - None
    """
    white: str | tuple[int, int, int] = 'white'
    yellow: str | tuple[int, int, int] = 'yellow'

