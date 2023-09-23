class Rectangle:
    """Class Rectangle."""

    def __init__(self, a, b):
        """The constructor accepts length and width."""
        self.__w = a
        self.__h = b

    def __str__(self):
        """String representation."""
        return f'Rectangle {self.__w} * {self.__h}'

    @property
    def size(self):
        return self.__w, self.__h

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, value):
        """Ability to change width rectangle"""
        if value < 0:
            raise ValueError("Value must be greate than zero")
        self.__w = value

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        """Ability to change length rectangle"""
        if value < 0:
            raise ValueError("Value must be greate than zero")
        self.__h = value


if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    r1.w = 5
    r1.h = 6
    print(r1.size)

    r1.w = -3
    r1.h = -2
    print(r1.size)
