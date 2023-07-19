"""
2.A triangle only exists if the sum of any two of its sides is greater than
third. Given a, b, c - the sides of the proposed triangle. It is required to
compare the length of each segment-side with the sum of the other two. If in at
least one case the segment is greater than the sum of the other two, then a
triangle with such sides does not exist. Separately report whether the triangle
is scalene, isosceles or equilateral.
"""


def is_triangle(a, b, c) -> bool:
    """ Сhecks whether the shape with the specified sides is a triangle """
    result = False
    if (a + b > c) and (b + c > a) and (a + c > b):
        result = True
    return result


def is_scalene(a, b, c):
    """ Checks if a triangle is scalene """
    result = False
    if (a != b) and (b != c) and (a != c):
        result = True
    return result


def is_equilateral(a, b, c):
    """ Checks if a triangle is equilateral """
    result = False
    if a == b == c:
        result = True
    return result


def get_type_triangle(a, b, c):
    if is_scalene(a, b, c):
        print("Разносторонний")
    elif is_equilateral(a, b, c):
        print("Равносторонний")
    else:
        print("Равнобедренный")


def check_triangle(a, b, c):
    if is_triangle(a, b, c):
        print("Треугольник существует")
        # whether the triangle is scalene, isosceles, or equilateral.
        get_type_triangle(a, b, c)
    else:
        print("Треугольник не существует")


if __name__ == '__main__':
    # the lengths of the sides of the triangle
    lengths_of_the_sides = [(5, 7, 3), (10, 5, 3), (5, 5, 5), (7, 7, 3)]
    for sides in lengths_of_the_sides:
        a, b, c = sides
        print(10 * "=")
        check_triangle(a, b, c)


    # check_triangle(5, 7, 3)  # Треугольник существует - тип Разносторонний
    # check_triangle(10, 5, 3)  # не существует
    # check_triangle(5, 5, 5)  # Треугольник существует - Равносторонний
    # check_triangle(7, 7, 3)  # Треугольник существует - Равнобедренный
