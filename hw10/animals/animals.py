from interfaces import NeedlesInterface, WingsInterface


class Animal:
    def __init__(self, name=None, age=0, skill=''):
        self.name = name
        self.age = age
        self.skill = skill

    def __str__(self):
        return (f'Animal: {self.__class__.__name__} - {self.name}.\n'
                f'Age: {self.age} year.\n'
                f'Skill: {self.skill}.')

    def do_something(self, how_many_times=1):
        text = f'I can {self.skill.lower()}'

        if how_many_times > 1:
            text += f' {how_many_times} times in a row'

        text += '.'
        print(text)


class AnimalFactory:
    def get_animal(self, type_, **params):
        if type_ == 'Fox':
            return Fox(**params)
        elif type_ == 'Cat':
            return Cat(**params)
        elif type_ == 'Fish':
            return Fish(**params)
        elif type_ == 'Bird':
            return Bird(**params)
        elif type_ == 'Hedgehog':
            return Hedgehog(**params)
        else:
            raise ValueError("There is no such animal")


class Fox(Animal):
    msg = 'tyaf-tyaf'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def say(self):
        print(f'Fox say: {self.msg}.')

    def do_something(self, how_many_times=1):
        print('Foxes are predatory animals.')
        super().do_something(how_many_times)


class Cat(Animal):
    def __init__(self, **kwargs):
        self.eyes_color = 'green'
        super().__init__(**kwargs)

    def __str__(self):
        description = super().__str__()
        description += f'\nIt has a beautiful {self.eyes_color} eyes.'
        return description


class Fish(Animal):
    def __init__(self, **kwargs):
        self.can_swim = True
        super().__init__(**kwargs)

    def fulfill_a_wish(self, wish):
        print('Abra-cadabra sim-salabim!')
        print(f'Your wish: {wish}.\nWish fulfilled!!!')

    def move_to_sea(self):
        text = f'Fish - {self.name} '
        if self.can_swim:
            text += 'move to sea. Goodbye!'
        else:
            text += "can't swim."
        print(text)


class Bird(Animal, WingsInterface):
    def fly(self):
        text = f'Bird - {self.name} '
        if self.has_wings and self.can_fly:
            text += 'flapping wings.'
        else:
            text += "can't fly."
        print(text)


class Hedgehog(Animal, NeedlesInterface):
    def get_answer(self):
        text = 'No!'
        if self.has_needles:
            text = 'Yes!'
        return text


if __name__ == '__main__':
    factory = AnimalFactory()

    # Fox
    fox_1 = factory.get_animal('Fox',
                               name='Lucy',
                               age=5,
                               skill='Hunt animals and birds well')

    fox_1.say()
    fox_1.do_something()

    # Cat
    cat_1 = factory.get_animal('Cat',
                               name='Murka',
                               age=1,
                               skill='Catch the mouse')
    print(cat_1)

    # Fish
    fish_1 = factory.get_animal('Fish',
                                name='Golden',
                                age=7,
                                skill='Swim in sea')
    print(fish_1)

    fish_1.fulfill_a_wish('Become the mistress of the sea')
    fish_1.move_to_sea()

    # Birds
    dove = factory.get_animal('Bird',
                              name='Dove Mapy',
                              age=2,
                              skill='Fly in the sky')
    print(dove)
    dove.fly()

    chicken = factory.get_animal('Bird',
                                 name='Chicken',
                                 age=3,
                                 skill='Laying eggs')
    chicken.can_fly = False
    print(chicken)
    chicken.fly()

    # Hedgehog
    hedgehog = factory.get_animal('Hedgehog',
                                  name='Timon',
                                  age=4,
                                  skill='The smartest animal')
    print(hedgehog)
    print(f'Does the hedgehog have needles? {hedgehog.get_answer()}')
