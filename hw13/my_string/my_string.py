import time

from my_string_exceptions import ZeroLengthStringError, OwnerTypeException


class MyString(str):
    """Class MyString."""

    def __new__(cls, value: str, owner: str):
        """Added the owner_name and create_time parameters."""
        instance = super().__new__(cls, value)
        instance.owner_name = owner
        instance.create_time = time.time()
        instance.value = value

        return instance

    def __str__(self):
        s = super().__str__()
        return (f"String: {s}. Owner: {self.owner_name}."
                f" Create: {self.create_time}")

    def __repr__(self):
        return f"MyString('{self.value}', '{self.owner_name}')"


if __name__ == "__main__":
    input_string = input('Enter your string: ')
    input_owner = input('Enter owner name: ')

    if len(input_owner) == 0 or len(input_string) == 0:
        raise ZeroLengthStringError

    if not input_owner.isalpha():
        raise OwnerTypeException

    s = MyString(input_string, input_owner)

    # For the programmer
    print(repr(s))
    # For user
    print(s)
