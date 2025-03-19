# Topic: Custom Classes in Python

class Rectangle:
    def __init__(self, length: int, width: int):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width
    
    def __iter__(self):
        """Make the Rectangle iterable."""
        yield {'length': self.length}
        yield {'width': self.width}