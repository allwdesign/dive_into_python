"""
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
📌Экземпляр должен запоминать последние k значений.
📌Параметр k передаётся при создании экземпляра.
📌Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.

Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
import json


class Factorial:
    def __init__(self, size):
        self.size = size
        self.__archive = []

    def __call__(self, num):
        fact = 1

        for i in range(1, num + 1):
            fact = fact * i

        if len(self.__archive) >= self.size:
            self.__archive.pop(0)

        self.__archive.append({num: fact})

        return fact

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('fact.json', 'w') as f:
            json.dump(self.__archive, f)

    def get_archive(self):
        return self.__archive


if __name__ == '__main__':
    f = Factorial(3)
    # print(f"The factorial of f(5) is : {f(5)}")
    # f(4)
    # f(2)
    # f(3)
    print(f.get_archive())
    with f as fact:
        print(fact(7))
        print(fact(6))
        print(fact(5))
        print(fact(4))
