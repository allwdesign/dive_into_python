def correct_input():
    """A function that requests numeric data from the user until he

    enters an integer or real number.
    """
    while True:
        try:
            num = float(input('Введите число: '))
            print('Успешно получили число')
            break
        except ValueError:
            print(f'Вы ввели не число!')

    return num


if __name__ == '__main__':
    print(correct_input())
