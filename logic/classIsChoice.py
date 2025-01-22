from dataclasses import dataclass

@dataclass
class IsChoice:
    """
    A simple class to represent a boolean choice that can be toggled.

    This class provides a single boolean attribute `isChoice` which can be
    toggled between `True` and `False` using the `changeIsChoice` property.

    Attributes:
        isChoice (bool): A boolean attribute that can be toggled.

    Methods:
        changeIsChoice: A property that toggles the `isChoice` attribute.
    """

    isChoice: bool = False

    @property
    def changeIsChoice(self):
        """
        Toggles the `isChoice` attribute between `True` and `False`.

        This property is used to change the value of the `isChoice` attribute
        to its opposite. For example, if `isChoice` is `True`, calling this
        property will set `isChoice` to `False`, and vice versa.

        Returns:
            None
        """
        self.isChoice = not self.isChoice
