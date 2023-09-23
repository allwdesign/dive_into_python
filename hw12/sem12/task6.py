"""
Изменяем класс прямоугольника.
📌Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Side:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not (self.min_length < value < self.max_length):
            raise ValueError("Value must be in a range")


class Rectangle:
    """Class Rectangle."""
    width = Side(0, 7)
    length = Side(2, 10)

    def __init__(self, a, b):
        """The constructor accepts length and width."""
        self.width = a
        self.length = b

    def __str__(self):
        """String representation."""
        return f'Rectangle {self.width} * {self.length}'


if __name__ == '__main__':
    r1 = Rectangle(2, 3)

    print(r1)
