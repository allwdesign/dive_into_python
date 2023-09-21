import json

from task3 import AccessErrorException, LevelException


class User:
    """Class User."""

    def __init__(self, name, id_, level):
        """Constructor."""
        self.name = name
        self.__id = id_
        self.level = level

    def __repr__(self):
        """String representation."""
        return f'Name: {self.name} Level: {self.level}'

    def __eq__(self, other):
        """Method compares users."""
        return (self.name == other.name) and (self.__id == other.__id)

    def __hash__(self):
        """Method for hashing."""
        return int(self.__id)


class Project:
    """Class Project."""

    def __init__(self):
        """Constructor."""
        self.users = self.load("users.json")
        self.entered_user = None

    def auth(self, name, id_, level):
        """Method for authenticate anonymous user."""
        anonymous = User(name, id_, level)
        if anonymous not in self.users:
            raise AccessErrorException

        for user in self.users:
            if user == anonymous:
                self.entered_user = user

    def add_user(self, name, id_, level):
        """Method for add new users to set."""
        if self.entered_user.level < level:
            raise LevelException

        self.users.add(User(name, id_, level))

    @staticmethod
    def load(file_name: str) -> set:
        """Load data about users from JSON file."""
        users = set()
        with open(file_name, 'r', encoding='utf-8') as f:
            json_file = json.load(f)

        for line in json_file:
            users.add(User(line['name'], line['id'], line['level']))

        return users


if __name__ == '__main__':
    project = Project()
    project.auth("Peter", "000456", 7)

    project.add_user("Natalya", "001345", 4)
    print(project.users)
