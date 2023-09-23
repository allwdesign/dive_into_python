import csv
import random


class Range:
    """Class descriptor Range."""

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if (self.min_value is not None) and not (value >= self.min_value):
            raise ValueError(f'Значение {value} должно быть больше или '
                             f'равно {self.min_value}')
        if (self.max_value is not None) and not (value <= self.max_value):
            raise ValueError(f'Значение {value} должно быть меньше или '
                             f'равно {self.max_value}')


class FIO:
    """Class descriptor FIO."""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str) or not value.isalpha():
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value[0].isupper():
            raise TypeError(f'Значение {value} должно быть с заглавной буквы')


class Point:
    """class Point."""

    test_point = Range(0, 100)
    class_point = Range(2, 5)

    def __init__(self, point=None, type_=None):
        if type_ == 'cp':
            self.class_point = point
            self.point = self.class_point
        elif type_ == 'tp':
            self.test_point = point
            self.point = self.test_point

    def __str__(self):
        return f'{self.point}'


class Subject:
    """Class Subject."""

    MIX_TEST_POINT = 0
    MAX_TEST_POINT = 100
    MIX_CLASS_POINT = 2
    MAX_CLASS_POINT = 5

    def __init__(self, title):
        self.title = title
        self.test_points = self.generate_points(self.MIX_TEST_POINT,
                                                self.MAX_TEST_POINT, 'tp')
        self.class_points = self.generate_points(self.MIX_CLASS_POINT,
                                                 self.MAX_CLASS_POINT, 'cp')

    def __str__(self):
        result = f'{self.title}:'
        if self.class_points:
            result += (f'\n\tclass points: '
                       f'{", ".join([p.__str__() for p in self.class_points])}'
                       f';')
        else:
            result += 'no class points, '

        if self.test_points:
            result += (f'\n\ttest points: '
                       f'{", ".join([p.__str__() for p in self.test_points])}'
                       f'.\n')
        else:
            result += 'no test points.\n'
        return result

    def generate_points(self, min_, max_, type_) -> list:
        points = []
        k = random.randint(0, 10)
        for i in range(0, 8 + k):
            # random test points
            point = random.randint(min_, max_)
            points.append(Point(point, type_))
        return points

    def add_test_point(self, point):
        self.test_points.append(Point(point, 'tp'))

    def add_class_point(self, point):
        self.class_points.append(Point(point, 'cp'))


class Student:
    """Class Student."""

    name = FIO()
    last_name = FIO()
    patronymic = FIO()
    age = Range(6, 19)
    grade = Range(1, 12)

    def __init__(self, last_name, name, patronymic, age, grade):
        self.__subjects = self.load()
        self.last_name = last_name
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.grade = grade

    def __repr__(self):
        return (f'Student(last_name={self.last_name}, name={self.name}, '
                f'patronymic={self.patronymic}, age = {self.age}, '
                f'grade={self.grade})')

    def __str__(self):
        return (f'Student: {self.last_name} {self.name} {self.patronymic}.\n'
                f'Age: {self.age}.\n'
                f'Grade: {self.grade}.')

    def report_average_test_scores(self):
        """for each subject"""
        for subject in self.__subjects:
            result = f'{subject.title}: '
            if subject.test_points:
                sum_points = sum(
                    [int(subj.point) for subj in subject.test_points])
                sub_avg = round(sum_points / len(subject.test_points), 1)
                result += f'average test scores: {sub_avg}.'
            else:
                result += 'There are no test grades for this subject.'
            print(result)

    def get_subjects(self):
        return self.__subjects

    def report_average_all_subjects(self):
        """for all subjects"""
        amount_all_points = 0
        sum_all_points = 0
        for subject in self.__subjects:
            if subject.class_points:
                amount_all_points += len(subject.class_points)
                points = [int(subj.point) for subj in subject.class_points]
                sum_subject_points = sum(points)
                sum_all_points += sum_subject_points

        return (f'Average class points for all subjects combined: '
                f'{round(sum_all_points / amount_all_points, 1)}')

    def load(self) -> list[Subject]:
        """Load data from csv file."""
        data = []
        with open('subjects.csv', 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.DictReader(f, fieldnames=['Subjects', ],
                                      dialect='excel',
                                      quoting=csv.QUOTE_NONNUMERIC)
            # Skipping the title line
            next(csv_file)

            for line in csv_file:
                data.append(Subject(line['Subjects']))
        return data


if __name__ == '__main__':
    student = Student('Ivanov', 'Petr', 'Ivanovich', 9, 2)
    print(student)

    print('===============Subjects===============')
    print(*student.get_subjects())
    print('======================================')

    student.report_average_test_scores()
    print(student.report_average_all_subjects())
