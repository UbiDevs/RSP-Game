from dataclasses import dataclass, field

@dataclass
class TextGroup:
    """
    TextGroup is a class designed to manage a collection of text objects. It provides a way to update all the text objects in the collection.

    Core functionality:
    - update(): Iterates through all text objects in the group and calls their update method.

    Example usage:
    """
    group: list = field(default_factory=list)
    
    def update(self):
        for obj in self.group:
            obj.update()
