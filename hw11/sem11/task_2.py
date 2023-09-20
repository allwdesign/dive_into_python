class Archive:
    """Archive class, which stores a couple of properties: a number and

    a string.
    """

    instance = None

    def __new__(cls, *args, **kwargs):
        """When creating a new instance of a class, old data from
        previously created instances is stored in a pair of archive
        lists.
        List archives are also instance properties.
        """
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_nums = []
        else:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_nums.append(cls.instance.number)
        return cls.instance

    def __init__(self, text: str, number: int):
        """Added the text and number parameters."""
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text: {self.text}. Number: {self.number}.'

    def __repr__(self):
        return f"Archive('{self.text}', '{self.number}')"


if __name__ == "__main__":
    archive_1 = Archive("Text 1", 5)
    archive_2 = Archive("Text 2", 8)
    archive_3 = Archive("Text 3", 11)
    # Old
    print(archive_1.old_text)
    print(archive_1.old_nums)
    # Current
    print(repr(archive_1))
    print(archive_3)
