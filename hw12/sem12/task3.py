"""
Создайте класс-генератор.
📌Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
📌Если переданы два параметра, считаем step=1.
📌Если передан один параметр, также считаем start=1.
"""

class FactorialGenerator:

    def __init__(self, *args):
        if len(args) == 3:
            self.start, self.stop, self.step = args
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        elif len(args) == 1:
            self.stop = args[0]
            self.start = 1
            self.step = 1


    def __iter__(self):
        return self

    def __next__(self):
        # Перебор чисел для которых будем считать факториал
        while self.start < self.stop:
            fact = 1
            # for generate factorial
            for i in range(1, self.start + 1):
                fact *= i
            self.start += 1
            return fact
        raise StopIteration


if __name__ == '__main__':
    fg = FactorialGenerator(1, 5, 1)
    for i in fg:
        print(i)
