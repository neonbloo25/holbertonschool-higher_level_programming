class Square:
    """
    Class Square that defines a square.
    
    Attributes:
        __size (int): the size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.
        
        Args:
            size (int): Size of the square, must be an integer >= 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        self.size = size  # Calls the setter to handle validation

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size to ensure it is an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
