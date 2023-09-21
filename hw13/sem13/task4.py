import json


class User:
    """Class User."""

    def __init__(self, name, id, level):
        """Constructor."""
        self.name = name
        self.__id = id
        self.level = level

    def __repr__(self):
        """String representation."""
        return f'Name: {self.name} Level: {self.level}'


def load(file_name: str) -> set:
    """Load data about users from JSON file."""
    users = set()
    with open(file_name, 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    for line in json_file:
        users.add(User(line['name'], line['id'], line['level']))

    return users


if __name__ == '__main__':
    print(load("users.json"))
