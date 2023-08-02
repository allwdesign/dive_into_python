import os


def parse(absolute_path: str) -> tuple:
    """Parse string with absolute path.

    A function that takes a string as input - the absolute path to
    the file and return the tuple: path, filename, extension.

    :param absolute_path: str
    :return: tuple
    """
    parts = absolute_path.split("/")
    filename, ext = parts[-1].split(".")
    path = "/".join(parts[:-1])

    return path, filename, ext


if __name__ == '__main__':
    print("Parse", parse("/home/natasha/social_network.sql"))

    # Alternative with os.path
    current_path, filename = os.path.split("/home/natasha/social_network.sql")
    ext = filename[-3:]

    print(tuple([current_path, filename[:-4], ext]))
